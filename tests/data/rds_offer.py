BASIC_RDS_W_EDITION_SKU = "UHQB4SMCY7W62UNV"
BASIC_RDS_WO_EDITION_SKU = "RYXYA7XK2PDKTNV4"

# One with databaseEdition and one without
BASIC_RDS_OFFER_DATA = [{
  "serviceCode": "AmazonRDS",
  "product": {
      "sku": "UHQB4SMCY7W62UNV",
      "productFamily": "Database Instance",
      "attributes": {
        "servicecode": "AmazonRDS",
        "location": "US West (Oregon)",
        "locationType": "AWS Region",
        "instanceType": "db.m4.large",
        "currentGeneration": "Yes",
        "instanceFamily": "General purpose",
        "vcpu": "2",
        "physicalProcessor": "Intel Xeon E5-2676 v3 (Haswell)",
        "clockSpeed": "2.4 GHz",
        "memory": "8 GiB",
        "storage": "EBS Only",
        "networkPerformance": "Moderate",
        "processorArchitecture": "64-bit",
        "engineCode": "3",
        "databaseEngine": "Oracle",
        "databaseEdition": "Standard One",
        "licenseModel": "Bring your own license",
        "deploymentOption": "Multi-AZ",
        "usagetype": "USW2-Multi-AZUsage:db.m4.large",
        "operation": "CreateDBInstance:0003",
        "dedicatedEbsThroughput": "450 Mbps",
        "enhancedNetworkingSupported": "Yes",
        "processorFeatures": "Intel AVX; Intel AVX2; Intel Turbo"
      },
  },
  "terms": {
    "Reserved": {
      "UHQB4SMCY7W62UNV.HU7G6KETJZ": {
        "offerTermCode": "HU7G6KETJZ",
        "sku": "UHQB4SMCY7W62UNV",
        "effectiveDate": "2015-10-31T23:59:59Z",
        "priceDimensions": {
          "UHQB4SMCY7W62UNV.HU7G6KETJZ.2TG2D8R56U": {
            "rateCode": "UHQB4SMCY7W62UNV.HU7G6KETJZ.2TG2D8R56U",
            "description": "Upfront Fee",
            "unit": "Quantity",
            "pricePerUnit": {
              "USD": "648"
            },
            "appliesTo": []
          },
          "UHQB4SMCY7W62UNV.HU7G6KETJZ.6YS6EN2CT7": {
            "rateCode": "UHQB4SMCY7W62UNV.HU7G6KETJZ.6YS6EN2CT7",
            "description": "Oracle SE1 (BYOL), db.m4.large instance-hours used this month",
            "beginRange": "0",
            "endRange": "Inf",
            "unit": "Hrs",
            "pricePerUnit": {
              "USD": "0.1120000000"
            },
            "appliesTo": []
          }
        },
        "termAttributes": {
          "LeaseContractLength": "1yr",
          "OfferingClass": "standard",
          "PurchaseOption": "Partial Upfront"
        }
      },
      "UHQB4SMCY7W62UNV.6QCMYABX3D": {
        "offerTermCode": "6QCMYABX3D",
        "sku": "UHQB4SMCY7W62UNV",
        "effectiveDate": "2015-10-31T23:59:59Z",
        "priceDimensions": {
          "UHQB4SMCY7W62UNV.6QCMYABX3D.6YS6EN2CT7": {
            "rateCode": "UHQB4SMCY7W62UNV.6QCMYABX3D.6YS6EN2CT7",
            "description": "USD 0.0 per Oracle SE1 (BYOL), db.m4.large instance-hour (or partial hour)",
            "beginRange": "0",
            "endRange": "Inf",
            "unit": "Hrs",
            "pricePerUnit": {
              "USD": "0.0000000000"
            },
            "appliesTo": []
          },
          "UHQB4SMCY7W62UNV.6QCMYABX3D.2TG2D8R56U": {
            "rateCode": "UHQB4SMCY7W62UNV.6QCMYABX3D.2TG2D8R56U",
            "description": "Upfront Fee",
            "unit": "Quantity",
            "pricePerUnit": {
              "USD": "1601"
            },
            "appliesTo": []
          }
        },
        "termAttributes": {
          "LeaseContractLength": "1yr",
          "OfferingClass": "standard",
          "PurchaseOption": "All Upfront"
        }
      }
    },
    "OnDemand": {
      "UHQB4SMCY7W62UNV.JRTCKXETXF": {
        "offerTermCode": "JRTCKXETXF",
        "sku": "UHQB4SMCY7W62UNV",
        "effectiveDate": "2017-03-01T00:00:00Z",
        "priceDimensions": {
          "UHQB4SMCY7W62UNV.JRTCKXETXF.6YS6EN2CT7": {
            "rateCode": "UHQB4SMCY7W62UNV.JRTCKXETXF.6YS6EN2CT7",
            "description": "$0.350 per RDS db.m4.large Multi-AZ instance hour (or partial hour) running Oracle SE1 (BYOL)",
            "beginRange": "0",
            "endRange": "Inf",
            "unit": "Hrs",
            "pricePerUnit": {
              "USD": "0.3500000000"
            },
            "appliesTo": []
          }
        },
        "termAttributes": {}
      }
    }
  }
}, {
  "serviceCode": "AmazonRDS",
  "product": {
    "sku": "RYXYA7XK2PDKTNV4",
    "productFamily": "Database Instance",
    "attributes": {
      "servicecode": "AmazonRDS",
      "location": "Asia Pacific (Tokyo)",
      "locationType": "AWS Region",
      "instanceType": "db.m4.large",
      "currentGeneration": "Yes",
      "instanceFamily": "General purpose",
      "vcpu": "2",
      "physicalProcessor": "Intel Xeon E5-2676 v3 (Haswell)",
      "clockSpeed": "2.4 GHz",
      "memory": "8 GiB",
      "storage": "EBS Only",
      "networkPerformance": "Moderate",
      "processorArchitecture": "64-bit",
      "engineCode": "18",
      "databaseEngine": "MariaDB",
      "licenseModel": "License included",
      "deploymentOption": "Single-AZ",
      "usagetype": "APN1-InstanceUsage:db.m4.large",
      "operation": "CreateDBInstance:0018",
      "dedicatedEbsThroughput": "450 Mbps",
      "enhancedNetworkingSupported": "Yes",
      "processorFeatures": "Intel AVX; Intel AVX2; Intel Turbo"
    }
  },
  "terms": {
    "Reserved": {
      "RYXYA7XK2PDKTNV4.HU7G6KETJZ": {
        "offerTermCode": "HU7G6KETJZ",
        "sku": "UHQB4SMCY7W62UNV",
        "effectiveDate": "2015-10-31T23:59:59Z",
        "priceDimensions": {
          "RYXYA7XK2PDKTNV4.HU7G6KETJZ.2TG2D8R56U": {
            "rateCode": "UHQB4SMCY7W62UNV.HU7G6KETJZ.2TG2D8R56U",
            "description": "Upfront Fee",
            "unit": "Quantity",
            "pricePerUnit": {
              "USD": "200"
            },
            "appliesTo": []
          },
          "RYXYA7XK2PDKTNV4.HU7G6KETJZ.6YS6EN2CT7": {
            "rateCode": "UHQB4SMCY7W62UNV.HU7G6KETJZ.6YS6EN2CT7",
            "description": "Oracle SE1 (BYOL), db.m4.large instance-hours used this month",
            "beginRange": "0",
            "endRange": "Inf",
            "unit": "Hrs",
            "pricePerUnit": {
              "USD": "0.1000000000"
            },
            "appliesTo": []
          }
        },
        "termAttributes": {
          "LeaseContractLength": "1yr",
          "OfferingClass": "standard",
          "PurchaseOption": "Partial Upfront"
        }
      },
      "RYXYA7XK2PDKTNV4.6QCMYABX3D": {
        "offerTermCode": "6QCMYABX3D",
        "sku": "UHQB4SMCY7W62UNV",
        "effectiveDate": "2015-10-31T23:59:59Z",
        "priceDimensions": {
          "UHQB4SMCY7W62UNV.6QCMYABX3D.6YS6EN2CT7": {
            "rateCode": "UHQB4SMCY7W62UNV.6QCMYABX3D.6YS6EN2CT7",
            "description": "USD 0.0 per Oracle SE1 (BYOL), db.m4.large instance-hour (or partial hour)",
            "beginRange": "0",
            "endRange": "Inf",
            "unit": "Hrs",
            "pricePerUnit": {
              "USD": "0.0000000000"
            },
            "appliesTo": []
          },
          "RYXYA7XK2PDKTNV4.6QCMYABX3D.2TG2D8R56U": {
            "rateCode": "UHQB4SMCY7W62UNV.6QCMYABX3D.2TG2D8R56U",
            "description": "Upfront Fee",
            "unit": "Quantity",
            "pricePerUnit": {
              "USD": "1601"
            },
            "appliesTo": []
          }
        },
        "termAttributes": {
          "LeaseContractLength": "1yr",
          "OfferingClass": "standard",
          "PurchaseOption": "All Upfront"
        }
      }
    },
    "OnDemand": {
      "RYXYA7XK2PDKTNV4.JRTCKXETXF": {
        "offerTermCode": "JRTCKXETXF",
        "sku": "UHQB4SMCY7W62UNV",
        "effectiveDate": "2017-03-01T00:00:00Z",
        "priceDimensions": {
          "UHQB4SMCY7W62UNV.JRTCKXETXF.6YS6EN2CT7": {
            "rateCode": "UHQB4SMCY7W62UNV.JRTCKXETXF.6YS6EN2CT7",
            "description": "$0.350 per RDS db.m4.large Multi-AZ instance hour (or partial hour) running Oracle SE1 (BYOL)",
            "beginRange": "0",
            "endRange": "Inf",
            "unit": "Hrs",
            "pricePerUnit": {
              "USD": "0.3500000000"
            },
            "appliesTo": []
          }
        },
        "termAttributes": {}
      }
    }
  }
}, ]
