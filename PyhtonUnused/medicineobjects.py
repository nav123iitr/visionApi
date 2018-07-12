import json
null = None
medicine={
#    "_id" : ObjectId("5a61e708ae8bdc453fea9f71"),
    "updated_by" : {
        "lastName" : "User",
        "_id" : 100001,
        "firstName" : "System"
    },
    "classification" : "HD",
    "is_product_active" : True,
    "brand_distribution" : "Respiratory",
    "brand_name" : "Cipla Limited",
#    "updated_at" : ISODate("2018-01-19T12:39:36.239Z"),
    "variant_count" : 1,
    "salts" : [ 
        {
            "name" : "Budesonide",
            "classification" : "HD",
            "dosage" : 0.0,
            "is_cold_storage" : False,
#            "id" : ObjectId("5a61a9bfae8bdc453fe990a9"),
            "unit" : "",
            "refill_index" : 1.0,
            "consumption_per_day" : 1.6,
            "disease" : "Asthma",
            "molecule_type" : "Antiasthmatic & Copd Preparations",
            "is_tele_consult" : True,
            "is_full_cource" : False,
            "max_order_quantity" : 100
        }
    ],
    "drug_category" : "DRUGS",
    "name" : "Budecort 0.5Mg Respules 2Ml",
    "is_habit_forming" : False,
#    "created_at" : ISODate("2018-01-19T12:39:36.239Z"),
    "created_by" : {
        "lastName" : "User",
        "_id" : 100001,
        "firstName" : "System"
    },
    "is_cold_storage" : False
}

Variant={
#    "_id" : ObjectId("5a61e708ae8bdc453fea9f72"),
    "comment" : "",
#    "updated_at" : ISODate("2018-01-19T12:39:36.248Z"),
    "drug_strength" : {},
    "pack_size" : {
        "unit" : "ML",
        "name" : "2ML",
        "value" : 2
    },
    "packaging_type" : "Temper Proof",
    "is_discontinue" : False,
    "replaced_variant" : null,
    "images" : [],
    "sku" : "029985",
    "eg_product_name" : "Budecort 0.5mg respules 2ml",
    "consumption_per_day" : 1.84,
    "created_by" : {
        "lastName" : "User",
        "_id" : 100001,
        "firstName" : "System"
    },
    "eg_sku" : "029985",
    "status" : "Active",
    "updated_by" : {
        "lastName" : "User",
        "_id" : 100001,
        "firstName" : "System"
    },
    "pack_type" : "RESPULES",
    "reason" : "",
    "is_available" : True,
    "product_id" : "5a61e708ae8bdc453fea9f71",
    "pack_size_unit" : "1",
    "name" : "Budecort 0.5mg respules 2ml",
#    "created_at" : ISODate("2018-01-19T12:39:36.248Z"),
    "is_cold_storage" : False,
    "is_retired" : False,
    "is_lc_assured_available" : True,
    "is_urgent_dl_available" : True
}



PriceFacility={

#    "_id" : ObjectId("5a61e708ae8bdc453fea9f73"),
    "status" : "Active",
    "updated_by" : {
        "lastName" : "User",
        "_id" : 100001,
        "firstName" : "System"
    },
    "selling_price" : 184.025,
#    "updated_at" : ISODate("2018-02-13T05:53:17.744Z"),
    "discount" : 15.0,
    "facility_id" : 101,
    "is_available" : True,
#    "variant_id" : ObjectId("5a61e708ae8bdc453fea9f72"),
    "sku" : "029985",
#    "created_at" : ISODate("2018-01-19T12:39:36.544Z"),
    "mrp" : 216.5,
    "rack_details" : "D-Y027",
    "created_by" : {
        "lastName" : "User",
        "_id" : 100001,
        "firstName" : "System"
    },
    "stock" : 855,
    "sync" : True,
    "pack_of" : 10.0
}
for res in medicine["salts"]:
    res2 = res["name"]
    print res2
#print medicine['salts']['name']
print "hello"