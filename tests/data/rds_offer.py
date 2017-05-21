BASIC_RDS_W_EDITION_SKU = "UHQB4SMCY7W62UNV"
BASIC_RDS_WO_EDITION_SKU = "RYXYA7XK2PDKTNV4"

# One with databaseEdition and one without
BASIC_RDS_OFFER_DATA =  {
  "offerCode": "AmazonRDS",
  "version": "20170419200300",
  "products": {
    "UHQB4SMCY7W62UNV": {
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
      }
    },
    "RYXYA7XK2PDKTNV4": {
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
    }
  },
  "terms": {
    "UHQB4SMCY7W62UNV": {
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
            "unit": "hrs",
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
      }
    },
    "RYXYA7XK2PDKTNV4": {
      "RYXYA7XK2PDKTNV4.4NA7Y494T4": {
        "offerTermCode": "4NA7Y494T4",
        "sku": "RYXYA7XK2PDKTNV4",
        "effectiveDate": "2015-10-31T23:59:59Z",
        "priceDimensions": {
          "RYXYA7XK2PDKTNV4.4NA7Y494T4.6YS6EN2CT7": {
            "rateCode": "RYXYA7XK2PDKTNV4.4NA7Y494T4.6YS6EN2CT7",
            "description": "MariaDB, db.m4.large instance-hours used this month",
            "beginRange": "0",
            "endRange": "Inf",
            "unit": "hrs",
            "pricePerUnit": {
              "USD": "0.1590000000"
            },
            "appliesTo": []
          }
        },
        "termAttributes": {
          "LeaseContractLength": "1yr",
          "OfferingClass": "standard",
          "PurchaseOption": "No Upfront"
        }
      }
    }
  }
}
