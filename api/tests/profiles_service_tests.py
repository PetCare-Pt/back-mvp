import pytest
from unittest.mock import Mock, patch
from datetime import datetime, timedelta
from pymongo.database import Collection
from bson.objectid import ObjectId
from models.models import ProProfile, Experience, Image, Certification, Address
from services.pro_profiles_service import create_profile, update_profile, verify_pro_profile_experience


@pytest.fixture
def mock_db():
    return Mock(spec=Collection)


@pytest.fixture
def valid_pro_profile() -> ProProfile:
    now = datetime.now()
    past = now - timedelta(days=365)
    return ProProfile(
        provider_id="provider123",
        profile_image="https://example.com/image.jpg",
        images=[
            Image(image_url="https://example.com/img1.jpg", detail="Detail 1")
        ],
        name="John Doe",
        description="Professional description",
        experience=Experience(start_date=past, end_date=now),
        certifications=[
            Certification(name="Cert1", certificate_url="https://example.com/cert1.jpg")
        ],
        addresses=[
            Address(city="City", address_detail="Detail")
        ]
    )


@pytest.fixture
def invalid_experience_future_start() -> ProProfile:
    now = datetime.now()
    future = now + timedelta(days=1)
    return ProProfile(
        provider_id="provider123",
        profile_image="https://example.com/image.jpg",
        images=[],
        name="John Doe",
        description="Description",
        experience=Experience(start_date=future),
        certifications=[],
        addresses=[Address(city="City", address_detail="Detail")]
    )


@pytest.fixture
def invalid_experience_end_before_start() -> ProProfile:
    now = datetime.now()
    past = now - timedelta(days=365)
    earlier = past - timedelta(days=1)
    return ProProfile(
        provider_id="provider123",
        profile_image="https://example.com/image.jpg",
        images=[],
        name="John Doe",
        description="Description",
        experience=Experience(start_date=past, end_date=earlier),
        certifications=[],
        addresses=[Address(city="City", address_detail="Detail")]
    )


class TestVerifyProProfileExperience:
    def test_valid_experience(self, valid_pro_profile: ProProfile):
        now = datetime.now()
        is_valid, msg = verify_pro_profile_experience(valid_pro_profile, now)
        assert is_valid is True
        assert msg is None

    def test_future_start_date(self, invalid_experience_future_start: ProProfile):
        now = datetime.now()
        is_valid, msg = verify_pro_profile_experience(invalid_experience_future_start, now)
        assert is_valid is False
        assert msg == "La fecha de inicio de la experiencia no puede ser posterior a la fecha actual"

    def test_end_date_before_start_date(self, invalid_experience_end_before_start: ProProfile):
        now = datetime.now()
        is_valid, msg = verify_pro_profile_experience(invalid_experience_end_before_start, now)
        assert is_valid is False
        assert msg == "La fecha de finalización de la experiencia no puede ser anterior a la fecha de inicio"


class TestCreateProfile:
    @patch('services.pro_profiles_service.model_to_db')
    def test_create_profile_success(self, mock_db, valid_pro_profile: ProProfile):
        mock_db.count_documents.return_value = 0
        mock_insert_result = Mock()
        mock_insert_result.inserted_id = "inserted_id_123"
        mock_db.insert_one.return_value = mock_insert_result

        result_id, msg = create_profile(valid_pro_profile, mock_db)

        assert result_id == "inserted_id_123"
        assert msg == "Perfil profesional creado exitosamente"
        mock_db.count_documents.assert_called_once_with({"provider_id": valid_pro_profile.provider_id})
        mock_db.insert_one.assert_called_once()
        assert valid_pro_profile.created_at is not None
        assert valid_pro_profile.updated_at is not None
        assert valid_pro_profile.is_active is True

    def test_create_profile_already_exists(self, mock_db, valid_pro_profile: ProProfile):
        mock_db.count_documents.return_value = 1

        result_id, msg = create_profile(valid_pro_profile, mock_db)

        assert result_id is None
        assert msg == "Ya has creado tu perfil profesional"
        mock_db.count_documents.assert_called_once_with({"provider_id": valid_pro_profile.provider_id})
        mock_db.insert_one.assert_not_called()

    def test_create_profile_invalid_experience(self, mock_db, invalid_experience_future_start: ProProfile):
        result_id, msg = create_profile(invalid_experience_future_start, mock_db)

        assert result_id is None
        assert msg == "La fecha de inicio de la experiencia no puede ser posterior a la fecha actual"
        mock_db.count_documents.assert_not_called()
        mock_db.insert_one.assert_not_called()


class TestUpdateProfile:
    @patch('services.pro_profiles_service.model_to_db')
    def test_update_profile_success(self, mock_db, valid_pro_profile: ProProfile):
        valid_pro_profile.id = "1234567890abcdef12345678"
        mock_db.count_documents.return_value = 1
        mock_update_result = Mock()
        mock_update_result.modified_count = 1
        mock_db.update_one.return_value = mock_update_result

        result_count, msg = update_profile(valid_pro_profile, mock_db)

        assert result_count == "1"
        assert msg == "Perfil profesional actualizado exitosamente"
        mock_db.count_documents.assert_called_once_with({"provider_id": valid_pro_profile.provider_id, 
                                                         "_id": ObjectId("1234567890abcdef12345678")})
        mock_db.update_one.assert_called_once()
        call_args, _ = mock_db.update_one.call_args
        set_data = call_args[1]["$set"]
        # Check that provider_id, created_at, is_active are removed from data_dict
        assert "provider_id" not in set_data
        assert "created_at" not in set_data
        assert "is_active" not in set_data
        assert valid_pro_profile.updated_at is not None

    def test_update_profile_not_exists(self, mock_db, valid_pro_profile: ProProfile):
        valid_pro_profile.id = "1234567890abcdef12345678"
        mock_db.count_documents.return_value = 0

        result_count, msg = update_profile(valid_pro_profile, mock_db)

        assert result_count is None
        assert msg == "No tienes un perfil profesional creado"
        mock_db.count_documents.assert_called_once()
        mock_db.update_one.assert_not_called()

    def test_update_profile_invalid_experience(self, mock_db, invalid_experience_future_start: ProProfile):
        invalid_experience_future_start.id = "1234567890abcdef12345678"
        result_count, msg = update_profile(invalid_experience_future_start, mock_db)

        assert result_count is None
        assert msg == "La fecha de inicio de la experiencia no puede ser posterior a la fecha actual"
        mock_db.count_documents.assert_not_called()
        mock_db.update_one.assert_not_called()
