
BASIC_EBS_OFFER_SKU = 'HY3BZPP2B6K8MSJF'
BASIC_IOPS_OFFER_SKU = 'D8RDVC722HKNR55G'
BASIC_EBS_OFFER_DATA = {
    'HY3BZPP2B6K8MSJF': {
        'serviceCode': 'AmazonEC2',
        'product': {
            'productFamily': 'Storage',
            'sku' : 'HY3BZPP2B6K8MSJF',
            'attributes' : {
                'servicecode' : 'AmazonEC2',
                'location' : 'US East (N. Virginia)',
                'locationType' : 'AWS Region',
                'storageMedia' : 'SSD-backed',
                'volumeType' : 'General Purpose',
                'maxVolumeSize' : '16 TiB',
                'maxIopsvolume' : '16000',
                'maxIopsBurstPerformance' : '3000 for volumes <= 1 TiB',
                'maxThroughputvolume' : '250 MiB/s',
                'usagetype' : 'EBS:VolumeUsage.gp2',
                'operation' : '',
                'servicename' : 'Amazon Elastic Compute Cloud'
            },
        },
        'terms': {
            'OnDemand': {
                'HY3BZPP2B6K8MSJF.JRTCKXETXF' : {
                    'offerTermCode' : 'JRTCKXETXF',
                    'sku' : 'HY3BZPP2B6K8MSJF',
                    'effectiveDate' : '2019-05-01T00:00:00Z',
                    'priceDimensions' : {
                        'HY3BZPP2B6K8MSJF.JRTCKXETXF.6YS6EN2CT7' : {
                            'rateCode' : 'HY3BZPP2B6K8MSJF.JRTCKXETXF.6YS6EN2CT7',
                            'description' : '$0.10 per GB-month of General Purpose SSD (gp2) provisioned storage - US East (Northern Virginia)',
                            'beginRange' : '0',
                            'endRange' : 'Inf',
                            'unit' : 'GB-Mo',
                            'pricePerUnit' : {
                                'USD' : '0.1000000000'
                            },
                            'appliesTo' : [ ]
                        }
                    },
                    "termAttributes" : { }
                }
            }
        }
    },
    'D8RDVC722HKNR55G' : {
        'servicecode' : 'AmazonEC2',
        'product' : {
            'productFamily' : 'System Operation',
            'sku' : 'D8RDVC722HKNR55G',
            'attributes' : {
                'servicecode' : 'AmazonEC2',
                'location' : 'US East (N. Virginia)',
                'locationType' : 'AWS Region',
                'provisioned' : 'Yes',
                'group' : 'EBS IOPS',
                'groupDescription' : 'IOPS',
                'usagetype' : 'EBS:VolumeP-IOPS.piops',
                'operation' : '',
                'servicename' : 'Amazon Elastic Compute Cloud'
            }
        },
        'terms': {
            'OnDemand': {
                'D8RDVC722HKNR55G.JRTCKXETXF' : {
                    'offerTermCode' : 'JRTCKXETXF',
                    'sku' : 'D8RDVC722HKNR55G',
                    'effectiveDate' : '2019-05-01T00:00:00Z',
                    'priceDimensions' : {
                        'D8RDVC722HKNR55G.JRTCKXETXF.6YS6EN2CT7' : {
                            'rateCode' : 'D8RDVC722HKNR55G.JRTCKXETXF.6YS6EN2CT7',
                            'description' : '$0.065 per IOPS-month provisioned - US East (Northern Virginia)',
                            'beginRange' : '0',
                            'endRange' : 'Inf',
                            'unit' : 'IOPS-Mo',
                            'pricePerUnit' : {
                                'USD' : '0.0650000000'
                            },
                            'appliesTo' : [ ]
                        }
                    },
                    "termAttributes" : { }
                }
            }
        }
    }
}
