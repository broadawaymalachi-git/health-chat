# Why each store produced no offers

## beyondhello — named things present but no price the parser recognizes -- PARSER GAP
- page: https://beyond-hello.com/specials
- json payloads: 2 (hosts: {'vfm4x0n23a-dsn.algolia.net': 1, 'api.iheartjane.com': 1})
- named, unpriced: '33 Weddings' keys=['brand', 'category', 'compound_names', 'description', 'name', 'root_types', 'searchable_slug', 'store_notes', 'unique_slug']
- named, unpriced: 'Apple Mintz' keys=['brand', 'category', 'compound_names', 'description', 'name', 'root_types', 'searchable_slug', 'store_notes', 'unique_slug']
- named, unpriced: 'Apricot Chem' keys=['brand', 'category', 'compound_names', 'description', 'name', 'root_types', 'searchable_slug', 'store_notes', 'unique_slug']
- named, unpriced: 'Banana OG [.75g]' keys=['brand', 'brand_subtype', 'category', 'compound_names', 'description', 'name', 'root_types', 'searchable_slug', 'store_notes', 'unique_slug']
- paths: specials[].conditions.bundle.independent.excluded_product_ids, specials[].conditions.bundle.independent.threshold_number_of_items_in_cart, specials[].conditions.bundle.independent.weights, specials[].conditions.bundle.dependent.excluded_product_ids, specials[].conditions.bundle.dependent.max_number_of_discounted_products, specials[].conditions.bundle.dependent.weights, specials[].conditions.bundle.settings.allow_discounts_on_required_products, specials[].conditions.bundle.settings.exclude_product_specials_from_bundle_qualifiers, specials[].conditions.bundle.settings.copy_conditions_for_discounted_products, specials[].conditions.bundle.settings.apply_target_price_per_unit, specials[].rules.settings.apply_target_price_per_unit, specials[].rules.settings.max_number_of_discounted_products

## cookies — page failed to load
- page: https://cookies.co/specials
- json payloads: 0 (hosts: none)
- error: Error: Page.goto: net::ERR_CERT_DATE_INVALID at https://cookies.co/specials
Call log:
  - navigating to "https://cookies.co/specials", waiting until "domcontentloaded"


## cultivate — named things present but no price the parser recognizes -- PARSER GAP
- page: https://cultivatelv.com/order-online
- json payloads: 5 (hosts: {'lab.alpineiq.com': 5})
- named, unpriced: 'Cultivate Spring Mountain' keys=['addr', 'city', 'country', 'customURL', 'customURLAndroid', 'embeddedMedURL', 'embeddedURL', 'globalID', 'id', 'isBrandStore', 'name', 'nickname', 'onlineShopURL', 'phone']
- named, unpriced: 'Cultivate Durango' keys=['addr', 'city', 'country', 'customURL', 'customURLAndroid', 'embeddedMedURL', 'embeddedURL', 'globalID', 'id', 'isBrandStore', 'name', 'nickname', 'onlineShopURL', 'phone']
- named, unpriced: 'Cultivate Sign Up Form (Updated Aug 2023)' keys=['coMarketing', 'created', 'gearfireWaiverDefSyncedAt', 'id', 'isDefault', 'legacyCreated', 'legacyID', 'name', 'popupWidget', 'sendTextOptIn', 'settingsMap', 'signupFields', 'updated', 'upgraded']
- named, unpriced: 'Join the Cultivate Garden! Sign up now!' keys=['brandName', 'buttonText', 'enableBrandName', 'enableCoverPhoto', 'enableLogo', 'images', 'pageStyle', 'style', 'subTitle', 'thankYouAction', 'title', 'waiverSettings', 'walletPassSettings']
- paths: data.appSettings.sharing.showShareInMenu, data.appSettings.productFeed, data.appSettings.productFeed.enabled, data.appSettings.productFeed.enableAndroid, data.appSettings.productFeed.showOnHomeTab, data.appSettings.productFeed.showOnShopTab, data.appSettings.verbiage.navigation.hamburgerMenu, data.appSettings.verbiage.navigation.hamburgerMenu.profileName, data.appSettings.verbiage.navigation.hamburgerMenu.shareAppName, data.appSettings.verbiage.navigation.hamburgerMenu.faqName

## curaleaf — JSON captured holds no menu data (wrong URL, or menu loads elsewhere)
- page: https://curaleaf.com/specials
- json payloads: 1 (hosts: {'curaleaf.com': 1})

## exhale — page failed to load
- page: https://exhalenv.com/specials
- json payloads: 0 (hosts: none)
- error: Error: Page.goto: net::ERR_NAME_NOT_RESOLVED at https://exhalenv.com/specials
Call log:
  - navigating to "https://exhalenv.com/specials", waiting until "domcontentloaded"


## greenlight — JSON captured holds no menu data (wrong URL, or menu loads elsewhere)
- page: https://greenlightdispensary.com/specials
- json payloads: 6 (hosts: {'script.crazyegg.com': 2, 'tags.srv.stackadapt.com': 1, 'cdn.acsbapp.com': 1, 'thegreenlightdispensary.info': 1, 'greenlightdispensary.com': 1})
- paths: widgetSettings.statementVariant

## inyo — 1 product-shaped nodes present -- parser should have caught these
- page: https://inyolasvegas.com/menu
- json payloads: 18 (hosts: {'api.nevada.getcarrot.io': 8})
- product-shaped nodes: 1
- named, unpriced: 'S. Maryland Pkwy' keys=['addressLine1', 'addressLine2', 'companyId', 'enabled', 'id', 'imageUrl', 'name', 'sort', 'timeZoneId']
- named, unpriced: 'S. Maryland Pkwy' keys=['addressLine1', 'addressLine2', 'companyId', 'enabled', 'id', 'imageUrl', 'name', 'sort', 'timeZoneId']
- named, unpriced: 'CONES (LIL LEAN)' keys=['batchId', 'batchName', 'brand', 'cacheTimestamp', 'carrotSubcategory', 'cashPriceRange', 'categoryName', 'categorySlug', 'description', 'descriptionAndroid', 'descriptionIos', 'effectTags', 'embedding', 'id']
- named, unpriced: 'INTEGRA BOOST 2 WAY HUMIDITY CONTROL PACK' keys=['batchId', 'batchName', 'brand', 'cacheTimestamp', 'carrotSubcategory', 'cashPriceRange', 'categoryName', 'categorySlug', 'description', 'descriptionAndroid', 'descriptionIos', 'effectTags', 'embedding', 'id']
- paths: results[].hits[].document.cashPriceRange, results[].hits[].document.option1Price, results[].hits[].document.unitWeight, results[].hits[].document.weights, refresh_product_recommendations, redemptionByProduct, pickup:min_price, minimum_item_price, surfside:product_list_zone_id, system:in_store_menu_dark_mode, system:in_store_menu_queue_image, system:in_store_menu_rotation

## jardin — page loaded but fetched no JSON (menu may be server-rendered, blocked, or behind a click)
- page: https://jardincannabis.com/specials
- json payloads: 0 (hosts: none)

## nevadamade — page loaded but fetched no JSON (menu may be server-rendered, blocked, or behind a click)
- page: https://nevadamademarijuana.com/specials
- json payloads: 0 (hosts: none)

## oasis — JSON captured holds no menu data (wrong URL, or menu loads elsewhere)
- page: https://oasiscannabis.com/specials
- json payloads: 7 (hosts: {'otlp-http-production.shopifysvc.com': 6, 'oasiscannabis.com': 1})

## planet13 — page loaded but fetched no JSON (menu may be server-rendered, blocked, or behind a click)
- page: https://planet13lasvegas.com/specials
- json payloads: 0 (hosts: none)

## reef — JSON captured holds no menu data (wrong URL, or menu loads elsewhere)
- page: https://reefdispensaries.com/specials
- json payloads: 1 (hosts: {'curaleaf.com': 1})

## rise — page loaded but fetched no JSON (menu may be server-rendered, blocked, or behind a click)
- page: https://risecannabis.com/specials
- json payloads: 0 (hosts: none)

## sanctuary — page loaded but fetched no JSON (menu may be server-rendered, blocked, or behind a click)
- page: https://sanctuarynv.com/specials
- json payloads: 0 (hosts: none)

## shango — page loaded but fetched no JSON (menu may be server-rendered, blocked, or behind a click)
- page: https://goshango.com/order-online
- json payloads: 0 (hosts: none)

## silverstate — page loaded but fetched no JSON (menu may be server-rendered, blocked, or behind a click)
- page: https://silverstaterelief.com/specials
- json payloads: 0 (hosts: none)

## thesource — named things present but no price the parser recognizes -- PARSER GAP
- page: https://www.thesourcenv.com/specials
- json payloads: 8 (hosts: {'lab.alpineiq.com': 6, 'ada.skynettechnologies.us': 2})
- named, unpriced: 'The Source Jane' keys=['connectionId', 'inventoryProvider', 'menuProvider', 'name']
- paths: data.ecomLocations[].subEcomLocations[].menuType, data.ecomLocations[].subEcomLocations[].ecomMenuProvider, data.ecomLocations[].ecomMenuProviders, data.ecomMenuProviders, data.menuType, data.recommendationSettings.screenSettings.price, data.recommendationSettings.screenSettings.price.enabled, data.recommendationSettings.screenSettings.price.required, data.recommendationSettings.screenSettings.price.edibleEnabled, data.recommendationSettings.screenSettings.price.edibleRequired, data.reviewSettings.screenSettings.productList, data.screenSettings.productDetails

## thrive — JSON captured holds no menu data (wrong URL, or menu loads elsewhere)
- page: https://thrivenevada.com/specials
- json payloads: 1 (hosts: {'zt6taxfu2g.execute-api.us-west-1.amazonaws.com': 1})

## treeoflife — page failed to load
- page: https://treeoflifedispensary.com/specials
- json payloads: 0 (hosts: none)
- error: Error: Page.goto: net::ERR_CONNECTION_CLOSED at https://treeoflifedispensary.com/specials
Call log:
  - navigating to "https://treeoflifedispensary.com/specials", waiting until "domcontentloaded"


## zenleaf — 512 product-shaped nodes present -- parser should have caught these
- page: https://zenleafdispensaries.com/menu
- json payloads: 13 (hosts: {'zenleafdispensaries.com': 4, 'data.zenleafdispensaries.com': 4})
- product-shaped nodes: 512
- named, unpriced: 'Abington' keys=['address_1', 'address_2', 'bodegaStore', 'city', 'hours', 'lat', 'lng', 'locationId', 'location_status', 'medicalStoreId', 'phoneNumberOverride', 'post_id', 'post_title', 'recreationalStoreId']
- named, unpriced: 'Altoona' keys=['address_1', 'address_2', 'bodegaStore', 'city', 'hours', 'lat', 'lng', 'locationId', 'location_status', 'medicalStoreId', 'phoneNumberOverride', 'post_id', 'post_title', 'recreationalStoreId']
- named, unpriced: 'Antwerp' keys=['address_1', 'address_2', 'bodegaStore', 'city', 'hours', 'lat', 'lng', 'locationId', 'location_status', 'medicalStoreId', 'phoneNumberOverride', 'post_id', 'post_title', 'recreationalStoreId']
- named, unpriced: 'Arcadia' keys=['address_1', 'address_2', 'bodegaStore', 'city', 'hours', 'lat', 'lng', 'locationId', 'location_status', 'medicalStoreId', 'phoneNumberOverride', 'post_id', 'post_title', 'recreationalStoreId']
- paths: products[].id, products[].name, products[].category, products[].category.id, products[].category.name, products[].category.canonicalName, products[].subcategory, products[].subcategory.id, products[].subcategory.name, products[].subcategory.canonicalName, products[].images, products[].brand
