
if __name__ == "__main__":
    import os
    from pymongo import MongoClient
    from dotenv import load_dotenv
    from datetime import datetime

    # Cargar las variables de entorno desde el archivo .env
    load_dotenv()

    # Leer la URL de conexión desde el archivo .env
    mongo_uri = os.getenv("MONGO_URI")

    # Conectarse a la base de datos MongoDB
    client = MongoClient(mongo_uri)
    db = client['petcare_db']

    # Crear la colección 'professional_profiles' si no existe
    db.create_collection('professional_profiles')

    # Datos de los perfiles profesionales
    profiles = [
        {
            "provider_id": "YqvvF1NMsPTtota8MnfBi2IZp7i1",
            "profile_image": "https://url_de_imagen_principal.com",
            "images": [
                {
                    "image_url": "https://url_de_imagen_adicional1.com",
                    "detail": "Imagen de un paseo con perros"
                },
                {
                    "image_url": "https://url_de_imagen_adicional2.com",
                    "detail": "Certificación en baño de mascotas"
                }
            ],
            "name": "Paseos y Cuidados Tunja",
            "description": "Ofrecemos servicios de paseos para mascotas, baños y cuidado personalizado para perros y gatos en Tunja.",
            "experience": {
                "start_date": datetime(2015, 5, 1),
                "end_date": None
            },
            "certifications": [
                {
                    "name": "Certificación en cuidado animal",
                    "certificate_url": "https://link_al_documento_certificacion.com"
                }
            ],
            "addresses": [
                {
                    "city": "Tunja",
                    "address_detail": "Carrera 10 #23-45, Barrio La Esperanza"
                }
            ],
            "created_at": datetime(2026, 3, 16),
            "updated_at": datetime(2026, 3, 16),
            "is_active": True
        },
        {
            "provider_id": "X4puf60MdTa3xGXJcQetJhzZ37B3",
            "profile_image": "https://url_de_imagen_principal2.com",
            "images": [
                {
                    "image_url": "https://url_de_imagen_adicional1_2.com",
                    "detail": "Baños de mascotas"
                }
            ],
            "name": "Baños y Paseos de Peludos",
            "description": "Servicio de baño y paseo para perros en Tunja, con atención personalizada.",
            "experience": {
                "start_date": datetime(2018, 3, 1),
                "end_date": None
            },
            "certifications": [
                {
                    "name": "Certificación en peluquería canina",
                    "certificate_url": "https://link_a_certificacion_peluqueria.com"
                }
            ],
            "addresses": [
                {
                    "city": "Tunja",
                    "address_detail": "Calle 22 #12-34, Barrio Los Andes"
                }
            ],
            "created_at": datetime(2026, 3, 16),
            "updated_at": datetime(2026, 3, 16),
            "is_active": True
        },
        {
            "provider_id": "4ceqVSGtQmgCsnb0P8mrUlXC0Ak1",
            "profile_image": "https://url_de_imagen_principal3.com",
            "images": [
                {
                    "image_url": "https://url_de_imagen_adicional1_3.com",
                    "detail": "Cuidado y paseo con mascotas"
                }
            ],
            "name": "Cuidado Animal Tunja",
            "description": "Cuidamos de tus mascotas mientras tú no estás, paseos y atención profesional para animales.",
            "experience": {
                "start_date": datetime(2017, 1, 15),
                "end_date": None
            },
            "certifications": [],
            "addresses": [
                {
                    "city": "Tunja",
                    "address_detail": "Avenida 5 #20-11, Barrio San Martin"
                }
            ],
            "created_at": datetime(2026, 3, 16),
            "updated_at": datetime(2026, 3, 16),
            "is_active": True
        },
        {
            "provider_id": "K75xexYeILhw16yrXiqgaXQ8rKF2",
            "profile_image": "https://url_de_imagen_principal4.com",
            "images": [
                {
                    "image_url": "https://url_de_imagen_adicional1_4.com",
                    "detail": "Servicios integrales para mascotas"
                }
            ],
            "name": "Servicios Integrales Mascotas",
            "description": "Brindamos servicios de paseo, baño y cuidado integral para tus mascotas en Tunja.",
            "experience": {
                "start_date": datetime(2016, 7, 10),
                "end_date": None
            },
            "certifications": [
                {
                    "name": "Certificación en paseos y cuidado",
                    "certificate_url": "https://link_a_certificacion_paseos.com"
                }
            ],
            "addresses": [
                {
                    "city": "Tunja",
                    "address_detail": "Calle 15 #8-33, Barrio El Bosque"
                }
            ],
            "created_at": datetime(2026, 3, 16),
            "updated_at": datetime(2026, 3, 16),
            "is_active": True
        }
    ]

    # Insertar los perfiles en la colección 'professional_profiles'
    db.professional_profiles.insert_many(profiles)

    print("Datos insertados correctamente en la base de datos.")    
