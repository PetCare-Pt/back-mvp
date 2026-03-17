db = db.getSiblingDB('petcare_db');
db.createCollection('professional_profiles');
db.createCollection('pets');
const now = new Date();
db.professional_profiles.insertMany([
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
      "start_date": new Date("2015-05-01"),
      "end_date": null
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
    "created_at": now,
    "updated_at": now,
    "is_active": true
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
      "start_date": new Date("2018-03-01"),
      "end_date": null
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
    "created_at": now,
    "updated_at": now,
    "is_active": true
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
      "start_date": new Date("2017-01-15"),
      "end_date": null
    },
    "certifications": [],
    "addresses": [
      {
        "city": "Tunja",
        "address_detail": "Avenida 5 #20-11, Barrio San Martin"
      }
    ],
    "created_at": now,
    "updated_at": now,
    "is_active": true
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
      "start_date": new Date("2016-07-10"),
      "end_date": null
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
    "created_at": now,
    "updated_at": now,
    "is_active": true
  }
]);
db.pets.insertMany([
  // Owner 1
  {
    owner_id: "YqvvF1NMsPTtota8MnfBi2IZp7i1",
    name: "Luna",
    image_url: "https://example.com/images/luna.jpg",
    species: "Perro",
    breed: "Labrador Retriever",
    birth_date: new Date("2020-05-10"),
    weight: 25.5,
    physical_description: "Pelaje amarillo, tamaño mediano, ojos marrones",
    special_notes: "Muy amigable, requiere paseos diarios",
    created_at: now,
    updatedAt: now,
    isActive: true
  },
  {
    owner_id: "YqvvF1NMsPTtota8MnfBi2IZp7i1",
    name: "Michi",
    image_url: "https://example.com/images/michi.jpg",
    species: "Gato",
    breed: "Siames",
    birth_date: new Date("2021-08-15"),
    weight: 4.2,
    physical_description: "Pelaje corto, blanco con manchas marrones",
    special_notes: "Le gusta estar en lugares altos",
    created_at: now,
    updatedAt: now,
    isActive: true
  },
  {
    owner_id: "YqvvF1NMsPTtota8MnfBi2IZp7i1",
    name: "Rocky",
    species: "Perro",
    breed: "Bulldog",
    birth_date: new Date("2019-03-20"),
    weight: 18.0,
    physical_description: "Robusto, cara arrugada",
    special_notes: "Problemas respiratorios leves",
    created_at: now,
    updatedAt: now,
    isActive: true
  },

  // Owner 2
  {
    owner_id: "K75xexYeILhw16yrXiqgaXQ8rKF2",
    name: "Max",
    image_url: "https://example.com/images/max.jpg",
    species: "Perro",
    breed: "Pastor Alemán",
    birth_date: new Date("2018-11-02"),
    weight: 30.0,
    physical_description: "Grande, pelaje negro y marrón",
    special_notes: "Entrenado para obediencia",
    created_at: now,
    updatedAt: now,
    isActive: true
  },
  {
    owner_id: "K75xexYeILhw16yrXiqgaXQ8rKF2",
    name: "Nina",
    species: "Gato",
    breed: "Persa",
    birth_date: new Date("2022-01-12"),
    weight: 3.8,
    physical_description: "Pelaje largo y blanco",
    special_notes: "Requiere cepillado diario",
    created_at: now,
    updatedAt: now,
    isActive: true
  },
  {
    owner_id: "K75xexYeILhw16yrXiqgaXQ8rKF2",
    name: "Coco",
    image_url: "https://example.com/images/coco.jpg",
    species: "Ave",
    breed: "Loro",
    birth_date: new Date("2020-07-07"),
    weight: 1.1,
    physical_description: "Plumas verdes con amarillo",
    special_notes: "Puede imitar sonidos",
    created_at: now,
    updatedAt: now,
    isActive: true
  }
]);
