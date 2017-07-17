
BASIC_EC2_OFFER_SKU = '4C7N4APU9GEUZ6H6'

# Includes one variation of the c4.xlarge product and just Partial Upfront RIs.
BASIC_EC2_OFFER_DATA = {
    'offerCode': 'AmazonEC2',
    'version': '20161213014831',
    'products': {
        '4C7N4APU9GEUZ6H6' : {
            'sku' : '4C7N4APU9GEUZ6H6',
            'productFamily' : 'Compute Instance',
            'attributes' : {
                'servicecode' : 'AmazonEC2',
                'location' : 'US East (N. Virginia)',
                'locationType' : 'AWS Region',
                'instanceType' : 'c4.large',
                'currentGeneration' : 'Yes',
                'instanceFamily' : 'Compute optimized',
                'vcpu' : '2',
                'physicalProcessor' : 'Intel Xeon E5-2666 v3 (Haswell)',
                'clockSpeed' : '2.9 GHz',
                'memory' : '3.75 GiB',
                'storage' : 'EBS only',
                'networkPerformance' : 'Moderate',
                'processorArchitecture' : '64-bit',
                'tenancy' : 'Shared',
                'operatingSystem' : 'Linux',
                'licenseModel' : 'No License required',
                'usagetype' : 'BoxUsage:c4.large',
                'operation' : 'RunInstances',
                'dedicatedEbsThroughput' : '500 Mbps',
                'enhancedNetworkingSupported' : 'Yes',
                'preInstalledSw' : 'NA',
                'processorFeatures' : 'Intel AVX; Intel AVX2; Intel Turbo'
            }
        },
    },
    'terms': {
        'OnDemand': {
            '4C7N4APU9GEUZ6H6' : {
                '4C7N4APU9GEUZ6H6.JRTCKXETXF' : {
                    'offerTermCode' : 'JRTCKXETXF',
                    'sku' : '4C7N4APU9GEUZ6H6',
                    'effectiveDate' : '2016-12-01T00:00:00Z',
                    'priceDimensions' : {
                        '4C7N4APU9GEUZ6H6.JRTCKXETXF.6YS6EN2CT7' : {
                            'rateCode' : '4C7N4APU9GEUZ6H6.JRTCKXETXF.6YS6EN2CT7',
                            'description' : '$0.1 per On Demand Linux c4.large Instance Hour',
                            'beginRange' : '0',
                            'endRange' : 'Inf',
                            'unit' : 'Hrs',
                            'pricePerUnit' : {
                                'USD' : '0.1000000000'
                            },
                            'appliesTo' : [ ]
                        }
                    },
                    'termAttributes' : { }
                }
            },
        },
        'Reserved': {
            "4C7N4APU9GEUZ6H6" : {
                "4C7N4APU9GEUZ6H6.HU7G6KETJZ" : {
                    "offerTermCode" : "HU7G6KETJZ",
                    "sku" : "4C7N4APU9GEUZ6H6",
                    "effectiveDate" : "2016-11-30T23:59:59Z",
                    "priceDimensions" : {
                        "4C7N4APU9GEUZ6H6.HU7G6KETJZ.6YS6EN2CT7" : {
                            "rateCode" : "4C7N4APU9GEUZ6H6.HU7G6KETJZ.6YS6EN2CT7",
                            "description" : "Linux/UNIX (Amazon VPC), c4.large instance-hours used this month",
                            "beginRange" : "0",
                            "endRange" : "Inf",
                            "unit" : "Hrs",
                            "pricePerUnit" : {
                                "USD" : "0.0300000000"
                            },
                            "appliesTo" : [ ]
                        },
                        "4C7N4APU9GEUZ6H6.HU7G6KETJZ.2TG2D8R56U" : {
                            "rateCode" : "4C7N4APU9GEUZ6H6.HU7G6KETJZ.2TG2D8R56U",
                            "description" : "Upfront Fee",
                            "unit" : "Quantity",
                            "pricePerUnit" : {
                                "USD" : "263"
                            },
                            "appliesTo" : [ ]
                        }
                    },
                    "termAttributes" : {
                        "LeaseContractLength" : "1yr",
                        "OfferingClass" : "standard",
                        "PurchaseOption" : "Partial Upfront"
                    }
                },
                "4C7N4APU9GEUZ6H6.38NPMPTW36" : {
                    "offerTermCode" : "38NPMPTW36",
                    "sku" : "4C7N4APU9GEUZ6H6",
                    "effectiveDate" : "2016-11-30T23:59:59Z",
                    "priceDimensions" : {
                        "4C7N4APU9GEUZ6H6.38NPMPTW36.2TG2D8R56U" : {
                            "rateCode" : "4C7N4APU9GEUZ6H6.38NPMPTW36.2TG2D8R56U",
                            "description" : "Upfront Fee",
                            "unit" : "Quantity",
                            "pricePerUnit" : {
                                "USD" : "539"
                            },
                            "appliesTo" : [ ]
                        },
                        "4C7N4APU9GEUZ6H6.38NPMPTW36.6YS6EN2CT7" : {
                            "rateCode" : "4C7N4APU9GEUZ6H6.38NPMPTW36.6YS6EN2CT7",
                            "description" : "Linux/UNIX (Amazon VPC), c4.large instance-hours used this month",
                            "beginRange" : "0",
                            "endRange" : "Inf",
                            "unit" : "Hrs",
                            "pricePerUnit" : {
                                "USD" : "0.0210000000"
                            },
                            "appliesTo" : [ ]
                        }
                    },
                    "termAttributes" : {
                        "LeaseContractLength" : "3yr",
                        "OfferingClass" : "standard",
                        "PurchaseOption" : "Partial Upfront"
                    }
                },
                "4C7N4APU9GEUZ6H6.R5XV2EPZQZ" : {
                    "offerTermCode" : "R5XV2EPZQZ",
                    "sku" : "4C7N4APU9GEUZ6H6",
                    "effectiveDate" : "2016-11-30T23:59:59Z",
                    "priceDimensions" : {
                        "4C7N4APU9GEUZ6H6.R5XV2EPZQZ.2TG2D8R56U" : {
                            "rateCode" : "4C7N4APU9GEUZ6H6.R5XV2EPZQZ.2TG2D8R56U",
                            "description" : "Upfront Fee",
                            "unit" : "Quantity",
                            "pricePerUnit" : {
                                "USD" : "710"
                            },
                            "appliesTo" : [ ]
                        },
                        "4C7N4APU9GEUZ6H6.R5XV2EPZQZ.6YS6EN2CT7" : {
                            "rateCode" : "4C7N4APU9GEUZ6H6.R5XV2EPZQZ.6YS6EN2CT7",
                            "description" : "Linux/UNIX (Amazon VPC), c4.large instance-hours used this month",
                            "beginRange" : "0",
                            "endRange" : "Inf",
                            "unit" : "Hrs",
                            "pricePerUnit" : {
                                "USD" : "0.0270000000"
                            },
                            "appliesTo" : [ ]
                        }
                    },
                    "termAttributes" : {
                        "LeaseContractLength" : "3yr",
                        "OfferingClass" : "convertible",
                        "PurchaseOption" : "Partial Upfront"
                    }
                },
                "4C7N4APU9GEUZ6H6.4NA7Y494T4" : {
                    "offerTermCode" : "4NA7Y494T4",
                    "sku" : "4C7N4APU9GEUZ6H6",
                    "effectiveDate" : "2017-04-30T23:59:59Z",
                    "priceDimensions" : {
                        "4C7N4APU9GEUZ6H6.4NA7Y494T4.6YS6EN2CT7" : {
                        "rateCode" : "4C7N4APU9GEUZ6H6.4NA7Y494T4.6YS6EN2CT7",
                        "description" : "Linux/UNIX (Amazon VPC), c4.large reserved instance applied",
                        "beginRange" : "0",
                        "endRange" : "Inf",
                        "unit" : "Hrs",
                        "pricePerUnit" : {
                            "USD" : "0.0630000000"
                        },
                        "appliesTo" : [ ]
                        }
                    },
                    "termAttributes" : {
                        "LeaseContractLength" : "1yr",
                        "OfferingClass" : "standard",
                        "PurchaseOption" : "No Upfront"
                    }
                },
            },
        }
    }
}
