from unittest.mock import MagicMock, patch
from datetime import datetime, date
from bson.objectid import ObjectId

from services.pets_profiles_service import create_profile, update_profile, verify_birthdate
from models.pets_profiles_models import PetProfile


class TestCreateProfile:
    @patch('services.pets_profiles_service.datetime')
    def test_create_profile_valid(self, mock_datetime):
        # Arrange
        mock_datetime.now.return_value = datetime(2023, 1, 1, 12, 0, 0)
        pet_profile = PetProfile(
            name="Fluffy",
            species="Dog",
            birth_date=date(2020, 1, 1),
            weight=10.5,
            owner_id="owner123"
        )
        db_mock = MagicMock()
        db_mock.insert_one.return_value.inserted_id = ObjectId("507f1f77bcf86cd799439011")

        # Act
        result_id, result_msg = create_profile(pet_profile, db_mock)

        # Assert
        assert result_id == "507f1f77bcf86cd799439011"
        assert result_msg == "Perfil de mascota creado exitosamente"
        db_mock.insert_one.assert_called_once()
        called_data = db_mock.insert_one.call_args[0][0]
        assert called_data["name"] == "Fluffy"
        assert called_data["is_active"] is True
        assert "created_at" in called_data
        assert "updated_at" in called_data

    @patch('services.pets_profiles_service.datetime')
    def test_create_profile_invalid_birthdate(self, mock_datetime):
        # Arrange
        mock_datetime.now.return_value = datetime(2023, 1, 1, 12, 0, 0)
        pet_profile = PetProfile(
            name="Fluffy",
            species="Dog",
            birth_date=date(2024, 1, 1),  # Future date
            weight=10.5,
            owner_id="owner123"
        )
        db_mock = MagicMock()

        # Act
        result_id, result_msg = create_profile(pet_profile, db_mock)

        # Assert
        assert result_id is None
        assert result_msg == "La fecha de nacimiento no puede ser posterior a la fecha actual"
        db_mock.insert_one.assert_not_called()


class TestUpdateProfile:
    @patch('services.pets_profiles_service.datetime')
    def test_update_profile_valid(self, mock_datetime):
        # Arrange
        mock_datetime.now.return_value = datetime(2023, 1, 1, 12, 0, 0)
        pet_profile = PetProfile(
            id="507f1f77bcf86cd799439011",
            name="Fluffy Updated",
            species="Dog",
            birth_date=date(2020, 1, 1),
            weight=12.0,
            owner_id="owner123",
            created_at=datetime(2022, 1, 1, 12, 0, 0),
            updated_at=datetime(2022, 1, 1, 12, 0, 0),
            is_active=True
        )
        db_mock = MagicMock()
        db_mock.update_one.return_value.modified_count = 1

        # Act
        result_count, result_msg = update_profile(pet_profile, db_mock)

        # Assert
        assert result_count == "1"
        assert result_msg == "Perfil de mascota actualizado exitosamente"
        db_mock.update_one.assert_called_once()
        args, _ = db_mock.update_one.call_args
        filter_arg, update_arg = args[0], args[1]
        assert filter_arg == {"owner_id": "owner123", "_id": ObjectId("507f1f77bcf86cd799439011")}
        assert "$set" in update_arg
        set_data = update_arg["$set"]
        assert set_data["name"] == "Fluffy Updated"
        assert "owner_id" not in set_data
        assert "created_at" not in set_data
        assert "is_active" not in set_data
        assert pet_profile.updated_at == datetime(2023, 1, 1, 12, 0, 0)

    @patch('services.pets_profiles_service.datetime')
    def test_update_profile_invalid_birthdate(self, mock_datetime):
        # Arrange
        mock_datetime.now.return_value = datetime(2023, 1, 1, 12, 0, 0)
        pet_profile = PetProfile(
            id="507f1f77bcf86cd799439011",
            name="Fluffy",
            species="Dog",
            birth_date=date(2024, 1, 1),  # Future date
            weight=10.5,
            owner_id="owner123"
        )
        db_mock = MagicMock()

        # Act
        result_count, result_msg = update_profile(pet_profile, db_mock)

        # Assert
        assert result_count is None
        assert result_msg == "La fecha de nacimiento no puede ser posterior a la fecha actual"
        db_mock.update_one.assert_not_called()


class TestVerifyBirthdate:
    def test_verify_birthdate_valid(self):
        # Arrange
        now = datetime(2023, 1, 1, 12, 0, 0)
        pet_profile = PetProfile(
            name="Fluffy",
            species="Dog",
            birth_date=date(2020, 1, 1),
            weight=10.5
        )

        # Act
        is_valid, msg = verify_birthdate(pet_profile, now)

        # Assert
        assert is_valid is True
        assert msg is None

    def test_verify_birthdate_invalid_future(self):
        # Arrange
        now = datetime(2023, 1, 1, 12, 0, 0)
        pet_profile = PetProfile(
            name="Fluffy",
            species="Dog",
            birth_date=date(2024, 1, 1),  # Future date
            weight=10.5
        )

        # Act
        is_valid, msg = verify_birthdate(pet_profile, now)

        # Assert
        assert is_valid is False
        assert msg == "La fecha de nacimiento no puede ser posterior a la fecha actual"

    def test_verify_birthdate_today(self):
        # Arrange
        now = datetime(2023, 1, 1, 12, 0, 0)
        pet_profile = PetProfile(
            name="Fluffy",
            species="Dog",
            birth_date=date(2023, 1, 1),  # Today
            weight=10.5
        )

        # Act
        is_valid, msg = verify_birthdate(pet_profile, now)

        # Assert
        assert is_valid is True
        assert msg is None
