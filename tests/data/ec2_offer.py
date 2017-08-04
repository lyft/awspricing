
BASIC_EC2_OFFER_SKU = '4C7N4APU9GEUZ6H6'
BASIC_EC2_OFFER_SKU_DATA_TRANSFER = '25KK9VY72V4RDJBD'
BASIC_EC2_OFFER_SKU_DEDICATED_HOST = '92WGTJSJZEKKZQCW'
BASIC_EC2_OFFER_SKU_FEE = 'URVAJM83XJ7HC9TD'
BASIC_EC2_OFFER_SKU_IP_ADDRESS = 'NDET67BXTNJGSGN2'
BASIC_EC2_OFFER_SKU_LOAD_BALANCER = 'BTECVTZRF9E9RBMN'
BASIC_EC2_OFFER_SKU_LOAD_BALANCER_APPLICATION = 'DJ56KTT4RXZCM5AC'
BASIC_EC2_OFFER_SKU_NAT_GATEWAY = '9F25CQRR8AA58QZS'
BASIC_EC2_OFFER_SKU_STORAGE_SNAPSHOT = '7U7TWP44UP36AT3R'
BASIC_EC2_OFFER_SKU_STORAGE = '4MB6SVGV7JKWFBUJ'
BASIC_EC2_OFFER_SKU_SYSTEM_OPERATION = '242K4UEGGQJM9QUQ'

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
        '25KK9VY72V4RDJBD': {
            'sku': '25KK9VY72V4RDJBD',
            'productFamily': 'Data Transfer',
            'attributes': {
                'transferType': 'InterRegion Outbound',
                'usagetype': 'USE2-SAE1-AWS-Out-Bytes',
                'toLocation': 'South America (Sao Paulo)',
                'fromLocation': 'US East (Ohio)',
                'servicecode': 'AWSDataTransfer',
                'toLocationType': 'AWS Region',
                'operation': '',
                'fromLocationType': 'AWS Region'
            }
        },
        '92WGTJSJZEKKZQCW': {
            'sku': '92WGTJSJZEKKZQCW',
            'productFamily': 'Dedicated Host',
            'attributes': {
                'physicalCores': '20',
                'operation': 'RunInstances',
                'instanceType': 'i2',
                'instanceCapacity8xlarge': '1',
                'vcpu': '32',
                'storage': 'NA',
                'preInstalledSw': 'NA',
                'location': 'US East (Ohio)',
                'memory': 'NA',
                'processorFeatures': 'Intel AVX; Intel Turbo',
                'instanceCapacity16xlarge': '1',
                'networkPerformance': 'NA',
                'usagetype': 'USE2-HostUsage:i2',
                'normalizationSizeFactor': 'NA',
                'processorArchitecture': '64-bit',
                'ecu': 'NA',
                'tenancy': 'Host',
                'servicecode': 'AmazonEC2',
                'instanceCapacityXlarge': '8',
                'instanceFamily': 'Storage optimized',
                'locationType': 'AWS Region',
                'licenseModel': 'No License required',
                'instanceCapacity2xlarge': '4',
                'instanceCapacity4xlarge': '2',
                'clockSpeed': '2.5 GHz',
                'physicalProcessor': 'Intel Xeon E5-2670 v2 (Ivy Bridge)',
                'operatingSystem': 'Linux'
            }
        },
        'URVAJM83XJ7HC9TD': {
            'sku': 'URVAJM83XJ7HC9TD',
            'productFamily': 'Fee',
            'attributes': {
                'group': 'EC2-Dedicated Usage',
                'locationType': 'AWS Region',
                'usagetype': 'SAE1-DedicatedUsage',
                'servicecode': 'AmazonEC2',
                'operation': 'Surcharge',
                'groupDescription': 'Fee for running at least one Dedicated Instance in the region',
                'location': 'South America (Sao Paulo)'
            }
        },
        'NDET67BXTNJGSGN2': {
            'sku': 'NDET67BXTNJGSGN2',
            'productFamily': 'IP Address',
            'attributes': {
                'group': 'ElasticIP:Address',
                'locationType': 'AWS Region',
                'usagetype': 'EU-ElasticIP:IdleAddress',
                'servicecode': 'AmazonEC2',
                'operation': '',
                'groupDescription': 'Elastic IP address attached to a running instance',
                'location': 'EU (Ireland)'
            }
        },
        'BTECVTZRF9E9RBMN': {
            'sku': 'BTECVTZRF9E9RBMN',
            'productFamily': 'Load Balancer',
            'attributes': {
                'group': 'ELB:Balancer',
                'locationType': 'AWS Region',
                'usagetype': 'USE2-DataProcessing-Bytes',
                'servicecode': 'AmazonEC2',
                'operation': 'LoadBalancing',
                'groupDescription': 'Data processed by Elastic Load Balancer',
                'location': 'US East (Ohio)'
            }
        },
        'DJ56KTT4RXZCM5AC': {
            'sku': 'DJ56KTT4RXZCM5AC',
            'productFamily': 'Load Balancer-Application',
            'attributes': {
                'group': 'ELB:Balancer',
                'locationType': 'AWS Region',
                'usagetype': 'CAN1-LoadBalancerUsage',
                'servicecode': 'AmazonEC2',
                'operation': 'LoadBalancing:Application',
                'groupDescription': 'LoadBalancer hourly usage by Application Load Balancer',
                'location': 'Canada (Central)'
            }
        },
        '9F25CQRR8AA58QZS': {
            'sku': '9F25CQRR8AA58QZS',
            'productFamily': 'NAT Gateway',
            'attributes': {
                'group': 'NGW:NatGateway',
                'locationType': 'AWS Region',
                'usagetype': 'EU-NatGateway-Prvd-Bytes',
                'servicecode': 'AmazonEC2',
                'operation': 'NatGateway',
                'groupDescription': 'Charge for per GB data processed by NAT Gateways with provisioned bandwidth',
                'location': 'EU (Ireland)'
            }
        },
        '7U7TWP44UP36AT3R': {
            'sku': '7U7TWP44UP36AT3R',
            'productFamily': 'Storage Snapshot',
            'attributes': {
                'locationType': 'AWS Region',
                'usagetype': 'EBS:SnapshotUsage',
                'servicecode': 'AmazonEC2',
                'storageMedia': 'Amazon S3',
                'operation': '',
                'location': 'US East (N. Virginia)'
            }
        },
        '4MB6SVGV7JKWFBUJ': {
            'sku': '4MB6SVGV7JKWFBUJ',
            'productFamily': 'Storage',
            'attributes': {
                'maxThroughputvolume': '160 MB/sec',
                'maxVolumeSize': '16 TiB',
                'locationType': 'AWS Region',
                'usagetype': 'APS3-EBS:VolumeUsage.gp2',
                'volumeType': 'General Purpose',
                'servicecode': 'AmazonEC2',
                'maxIopsBurstPerformance': '3000 for volumes <= 1 TiB',
                'storageMedia': 'SSD-backed',
                'maxIopsvolume': '10000',
                'operation': '',
                'location': 'Asia Pacific (Mumbai)'
            }
        },
        '242K4UEGGQJM9QUQ': {
            'sku': '242K4UEGGQJM9QUQ',
            'productFamily': 'System Operation',
            'attributes': {
                'provisioned': 'Yes',
                'group': 'EBS IOPS',
                'locationType': 'AWS Region',
                'usagetype': 'EUW2-EBS:VolumeP-IOPS.piops',
                'comments': 'To be made public at the time of LHR launch, 12/13',
                'servicecode': 'AmazonEC2',
                'operation': '',
                'groupDescription': 'IOPS',
                'location': 'EU (London)'
            }
        }
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
            '25KK9VY72V4RDJBD': {
                '25KK9VY72V4RDJBD.JRTCKXETXF': {
                    'sku': '25KK9VY72V4RDJBD',
                    'termAttributes': {},
                    'effectiveDate': '2017-07-01T00:00:00Z',
                    'offerTermCode': 'JRTCKXETXF',
                    'priceDimensions': {
                        '25KK9VY72V4RDJBD.JRTCKXETXF.6YS6EN2CT7': {
                            'description': '$0.02 per GB - US East (Ohio) data transfer to South America (Sao Paulo)',
                            'pricePerUnit': {
                                'USD': '0.0200000000'
                            },
                            'rateCode': '25KK9VY72V4RDJBD.JRTCKXETXF.6YS6EN2CT7',
                            'endRange': 'Inf',
                            'beginRange': '0',
                            'appliesTo': [],
                            'unit': 'GB'
                        }
                    }
                }
            },
            '92WGTJSJZEKKZQCW': {
                '92WGTJSJZEKKZQCW.JRTCKXETXF': {
                    'sku': '92WGTJSJZEKKZQCW',
                    'termAttributes': {},
                    'effectiveDate': '2017-07-01T00:00:00Z',
                    'offerTermCode': 'JRTCKXETXF',
                    'priceDimensions': {
                        '92WGTJSJZEKKZQCW.JRTCKXETXF.6YS6EN2CT7': {
                            'description': '$7.502 per On Demand I2 Dedicated Host Hour',
                            'pricePerUnit': {
                                'USD': '7.5020000000'
                            },
                            'rateCode': '92WGTJSJZEKKZQCW.JRTCKXETXF.6YS6EN2CT7',
                            'endRange': 'Inf',
                            'beginRange': '0',
                            'appliesTo': [],
                            'unit': 'Hrs'
                        }
                    }
                }
            },
            'URVAJM83XJ7HC9TD': {
                'URVAJM83XJ7HC9TD.JRTCKXETXF': {
                    'sku': 'URVAJM83XJ7HC9TD',
                    'termAttributes': {},
                    'effectiveDate': '2017-07-01T00:00:00Z',
                    'offerTermCode': 'JRTCKXETXF',
                    'priceDimensions': {
                        'URVAJM83XJ7HC9TD.JRTCKXETXF.6YS6EN2CT7': {
                            'description': '$2.00 once per hour when you\'re running at least one Dedicated Instance in the South America(Sao Paulo) Region ',
                            'pricePerUnit': {
                                'USD': '2.0000000000'
                            },
                            'rateCode': 'URVAJM83XJ7HC9TD.JRTCKXETXF.6YS6EN2CT7',
                            'endRange': 'Inf',
                            'beginRange': '0',
                            'appliesTo': [],
                            'unit': 'Hrs'
                        }
                    }
                }
            },
            'NDET67BXTNJGSGN2': {
                'NDET67BXTNJGSGN2.JRTCKXETXF': {
                    'sku': 'NDET67BXTNJGSGN2',
                    'termAttributes': {},
                    'effectiveDate': '2017-07-01T00:00:00Z',
                    'offerTermCode': 'JRTCKXETXF',
                    'priceDimensions': {
                        'NDET67BXTNJGSGN2.JRTCKXETXF.8EEUB22XNJ': {
                            'description': '$0.00 per Elastic IP address not attached to a running instance for the first hour',
                            'pricePerUnit': {
                                'USD': '0.0000000000'
                            },
                            'rateCode': 'NDET67BXTNJGSGN2.JRTCKXETXF.8EEUB22XNJ',
                            'endRange': '1',
                            'beginRange': '0',
                            'appliesTo': [],
                            'unit': 'Hrs'
                        },
                        'NDET67BXTNJGSGN2.JRTCKXETXF.JTU8TKNAMW': {
                            'description': '$0.005 per Elastic IP address not attached to a running instance per hour (prorated)',
                            'pricePerUnit': {
                                'USD': '0.0050000000'
                            },
                            'rateCode': 'NDET67BXTNJGSGN2.JRTCKXETXF.JTU8TKNAMW',
                            'endRange': 'Inf',
                            'beginRange': '1',
                            'appliesTo': [],
                            'unit': 'Hrs'
                        }
                    }
                }
            },
            'BTECVTZRF9E9RBMN': {
                'BTECVTZRF9E9RBMN.JRTCKXETXF': {
                    'sku': 'BTECVTZRF9E9RBMN',
                    'termAttributes': {},
                    'effectiveDate': '2017-07-01T00:00:00Z',
                    'offerTermCode': 'JRTCKXETXF',
                    'priceDimensions': {
                        'BTECVTZRF9E9RBMN.JRTCKXETXF.6YS6EN2CT7': {
                            'description': '$0.008 per GB Data Processed by the LoadBalancer',
                            'pricePerUnit': {
                                'USD': '0.0080000000'
                            },
                            'rateCode': 'BTECVTZRF9E9RBMN.JRTCKXETXF.6YS6EN2CT7',
                            'endRange': 'Inf',
                            'beginRange': '0',
                            'appliesTo': [],
                            'unit': 'GB'
                        }
                    }
                }
            },
            'DJ56KTT4RXZCM5AC': {
                'DJ56KTT4RXZCM5AC.JRTCKXETXF': {
                    'sku': 'DJ56KTT4RXZCM5AC',
                    'termAttributes': {},
                    'effectiveDate': '2017-07-01T00:00:00Z',
                    'offerTermCode': 'JRTCKXETXF',
                    'priceDimensions': {
                        'DJ56KTT4RXZCM5AC.JRTCKXETXF.6YS6EN2CT7': {
                            'description': '$0.02475 per Application LoadBalancer-hour (or partial hour)',
                            'pricePerUnit': {
                                'USD': '0.0247500000'
                            },
                            'rateCode': 'DJ56KTT4RXZCM5AC.JRTCKXETXF.6YS6EN2CT7',
                            'endRange': 'Inf',
                            'beginRange': '0',
                            'appliesTo': [],
                            'unit': 'Hrs'
                        }
                    }
                }
            },
            '9F25CQRR8AA58QZS': {
                '9F25CQRR8AA58QZS.JRTCKXETXF': {
                    'sku': '9F25CQRR8AA58QZS',
                    'termAttributes': {},
                    'effectiveDate': '2017-07-01T00:00:00Z',
                    'offerTermCode': 'JRTCKXETXF',
                    'priceDimensions': {
                        '9F25CQRR8AA58QZS.JRTCKXETXF.6YS6EN2CT7': {
                            'description': '$0.00 per GB Data Processed by NAT Gateways with Provisioned Bandwidth',
                            'pricePerUnit': {
                                'USD': '0.0000000000'
                            },
                            'rateCode': '9F25CQRR8AA58QZS.JRTCKXETXF.6YS6EN2CT7',
                            'endRange': 'Inf',
                            'beginRange': '0',
                            'appliesTo': [],
                            'unit': 'GB'
                        }
                    }
                }
            },
            '7U7TWP44UP36AT3R': {
                '7U7TWP44UP36AT3R.JRTCKXETXF': {
                    'sku': '7U7TWP44UP36AT3R',
                    'termAttributes': {},
                    'effectiveDate': '2017-07-01T00:00:00Z',
                    'offerTermCode': 'JRTCKXETXF',
                    'priceDimensions': {
                        '7U7TWP44UP36AT3R.JRTCKXETXF.6YS6EN2CT7': {
                            'description': '$0.05 per GB-Month of snapshot data stored - US East (Northern Virginia)',
                            'pricePerUnit': {
                                'USD': '0.0500000000'
                            },
                            'rateCode': '7U7TWP44UP36AT3R.JRTCKXETXF.6YS6EN2CT7',
                            'endRange': 'Inf',
                            'beginRange': '0',
                            'appliesTo': [],
                            'unit': 'GB-Mo'
                        }
                    }
                }
            },
            '4MB6SVGV7JKWFBUJ': {
                '4MB6SVGV7JKWFBUJ.JRTCKXETXF': {
                    'sku': '4MB6SVGV7JKWFBUJ',
                    'termAttributes': {},
                    'effectiveDate': '2017-07-01T00:00:00Z',
                    'offerTermCode': 'JRTCKXETXF',
                    'priceDimensions': {
                        '4MB6SVGV7JKWFBUJ.JRTCKXETXF.6YS6EN2CT7': {
                            'description': '$0.114 per GB-month of General Purpose SSD (gp2) provisioned storage - Asia Pacific (Mumbai)',
                            'pricePerUnit': {
                                'USD': '0.1140000000'
                            },
                            'rateCode': '4MB6SVGV7JKWFBUJ.JRTCKXETXF.6YS6EN2CT7',
                            'endRange': 'Inf',
                            'beginRange': '0',
                            'appliesTo': [],
                            'unit': 'GB-Mo'
                        }
                    }
                }
            },
            '242K4UEGGQJM9QUQ': {
                '242K4UEGGQJM9QUQ.JRTCKXETXF': {
                    'sku': '242K4UEGGQJM9QUQ',
                    'termAttributes': {},
                    'effectiveDate': '2017-07-01T00:00:00Z',
                    'offerTermCode': 'JRTCKXETXF',
                    'priceDimensions': {
                        '242K4UEGGQJM9QUQ.JRTCKXETXF.6YS6EN2CT7': {
                            'description': '$0.076 per IOPS-month provisioned - EU (London)',
                            'pricePerUnit': {
                                'USD': '0.0760000000'
                            },
                            'rateCode': '242K4UEGGQJM9QUQ.JRTCKXETXF.6YS6EN2CT7',
                            'endRange': 'Inf',
                            'beginRange': '0',
                            'appliesTo': [],
                            'unit': 'IOPS-Mo'
                        }
                    }
                }
            }
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
