# Changelog

## 1.1.5

 * Add capacitystatus attribute for EC2 (#29)

## 1.1.4

 * Include bare metal instance offers for EC2 (#19)

## 1.1.3

 * Fix a bug with the case of dimension units (#16)

## 1.1.2

* Ignore sku's with unexpected format (#15)
* Add optional version input for offers to support changing to non-current pricing list (#15)

## 1.1.1

* Fix a bug with reserved costs and a No Upfront purchase option (#11)

## 1.1.0

* Add support for RDS helpers (#9)

## 1.0.2

* Add extra filter options (tenancy, license_model, preinstalled_software) when fetching EC2 reserved prices (#4)
* Fix a bug where attribute collisions would cause an exception on offer instantiation (#5)

## 1.0.0

* Initial release
