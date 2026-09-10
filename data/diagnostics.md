# Why each store produced no offers

## beyondhello — blocked before the menu loaded (near-empty document)
- page: https://beyond-hello.com/deals
- json payloads: 0 (hosts: none)

## cookies — page failed to load
- page: https://cookies.co/products
- json payloads: 0 (hosts: none)
- error: Error: Page.goto: net::ERR_CERT_DATE_INVALID at https://cookies.co/products
Call log:
  - navigating to "https://cookies.co/products", waiting until "domcontentloaded"


## cultivate — named things present but no price the parser recognizes -- PARSER GAP
- page: https://cultivatelv.com/order-online
- json payloads: 5 (hosts: {'lab.alpineiq.com': 5})
- named, unpriced: 'Cultivate Spring Mountain' keys=['addr', 'city', 'country', 'customURL', 'customURLAndroid', 'embeddedMedURL', 'embeddedURL', 'globalID', 'id', 'isBrandStore', 'name', 'nickname', 'onlineShopURL', 'phone']
- named, unpriced: 'Cultivate Durango' keys=['addr', 'city', 'country', 'customURL', 'customURLAndroid', 'embeddedMedURL', 'embeddedURL', 'globalID', 'id', 'isBrandStore', 'name', 'nickname', 'onlineShopURL', 'phone']
- named, unpriced: 'Cultivate Sign Up Form (Updated Aug 2023)' keys=['coMarketing', 'created', 'gearfireWaiverDefSyncedAt', 'id', 'isDefault', 'legacyCreated', 'legacyID', 'name', 'popupWidget', 'sendTextOptIn', 'settingsMap', 'signupFields', 'updated', 'upgraded']
- named, unpriced: 'Join the Cultivate Garden! Sign up now!' keys=['brandName', 'buttonText', 'enableBrandName', 'enableCoverPhoto', 'enableLogo', 'images', 'pageStyle', 'style', 'subTitle', 'thankYouAction', 'title', 'waiverSettings', 'walletPassSettings']
- paths: data.appSettings.sharing.showShareInMenu, data.appSettings.productFeed, data.appSettings.productFeed.enabled, data.appSettings.productFeed.enableAndroid, data.appSettings.productFeed.showOnHomeTab, data.appSettings.productFeed.showOnShopTab, data.appSettings.verbiage.navigation.hamburgerMenu, data.appSettings.verbiage.navigation.hamburgerMenu.profileName, data.appSettings.verbiage.navigation.hamburgerMenu.shareAppName, data.appSettings.verbiage.navigation.hamburgerMenu.faqName

## curaleaf — JSON captured holds no menu data (wrong URL, or menu loads elsewhere)
- page: https://curaleaf.com/products
- json payloads: 1 (hosts: {'curaleaf.com': 1})

## exhale — page failed to load
- page: https://exhalenv.com/products
- json payloads: 0 (hosts: none)
- error: Error: Page.goto: net::ERR_NAME_NOT_RESOLVED at https://exhalenv.com/products
Call log:
  - navigating to "https://exhalenv.com/products", waiting until "domcontentloaded"


## greenlight — JSON captured holds no menu data (wrong URL, or menu loads elsewhere)
- page: https://greenlightdispensary.com/products
- json payloads: 5 (hosts: {'script.crazyegg.com': 2, 'cdn.acsbapp.com': 1, 'tags.srv.stackadapt.com': 1, 'thegreenlightdispensary.info': 1})
- paths: widgetSettings.statementVariant

## inyo — 1 product-shaped nodes present -- parser should have caught these
- page: https://inyolasvegas.com/menu
- json payloads: 18 (hosts: {'api.nevada.getcarrot.io': 8})
- product-shaped nodes: 1
- named, unpriced: 'S. Maryland Pkwy' keys=['addressLine1', 'addressLine2', 'companyId', 'enabled', 'id', 'imageUrl', 'name', 'sort', 'timeZoneId']
- named, unpriced: 'S. Maryland Pkwy' keys=['addressLine1', 'addressLine2', 'companyId', 'enabled', 'id', 'imageUrl', 'name', 'sort', 'timeZoneId']
- named, unpriced: 'CONES (LIL LEAN)' keys=['batchId', 'batchName', 'brand', 'cacheTimestamp', 'carrotSubcategory', 'cashPriceRange', 'categoryName', 'categorySlug', 'description', 'descriptionAndroid', 'descriptionIos', 'effectTags', 'embedding', 'id']
- named, unpriced: 'INTEGRA BOOST 2 WAY HUMIDITY CONTROL PACK' keys=['batchId', 'batchName', 'brand', 'cacheTimestamp', 'carrotSubcategory', 'cashPriceRange', 'categoryName', 'categorySlug', 'description', 'descriptionAndroid', 'descriptionIos', 'effectTags', 'embedding', 'id']
- paths: results[].hits[].document.cashPriceRange, results[].hits[].document.option1Price, results[].hits[].document.unitWeight, results[].hits[].document.weights, pickup:min_price, minimum_item_price, surfside:product_list_zone_id, system:in_store_menu_dark_mode, system:in_store_menu_queue_image, system:in_store_menu_rotation, system:in_store_menu_background, refresh_product_recommendations

## jardin — blocked before the menu loaded (HTTP 404)
- page: https://jardincannabis.com/products
- json payloads: 0 (hosts: none)

## leafly_deals — 6 product-shaped nodes present -- parser should have caught these
- page: https://www.leafly.com/deals/las-vegas-nv-us
- json payloads: 2 (hosts: {'www.leafly.com': 1, 'consumer-api.leafly.com': 1})
- product-shaped nodes: 6
- named, unpriced: "5 for $35 Solaris 1g Flower Mix'n'Match" keys=['active', 'buyQuantity', 'cadence', 'daysOfWeek', 'dealSegments', 'dealTiers', 'discountAmount', 'discountLabel', 'discountType', 'dispensary', 'dispensaryTimeZone', 'endsAt', 'finePrint', 'getQuantity']
- named, unpriced: 'The Sanctuary - North Las Vegas' keys=['distanceMi', 'hasDeliveryEnabled', 'hasReservationsEnabled', 'id', 'locations', 'name', 'primaryLocation', 'slug', 'timeZone']
- named, unpriced: '5/$35 on ALL $10 Prerolls!' keys=['active', 'buyQuantity', 'cadence', 'daysOfWeek', 'dealSegments', 'dealTiers', 'discountAmount', 'discountLabel', 'discountType', 'dispensary', 'dispensaryTimeZone', 'endsAt', 'finePrint', 'getQuantity']
- named, unpriced: 'The Sanctuary - North Las Vegas' keys=['distanceMi', 'hasDeliveryEnabled', 'hasReservationsEnabled', 'id', 'locations', 'name', 'primaryLocation', 'slug', 'timeZone']
- priced, unnamed: $10.0 keys=['cartQuantity', 'cartUnit', 'cbdPips', 'deal', 'dealId', 'displayQuantity', 'externalKey', 'id', 'medical', 'normalizedQuantityLabel', 'offers', 'price', 'pricePerUnit', 'quantity']
- priced, unnamed: $10.0 keys=['cartQuantity', 'cartUnit', 'cbdPips', 'deal', 'dealId', 'displayQuantity', 'externalKey', 'id', 'medical', 'normalizedQuantityLabel', 'offers', 'price', 'pricePerUnit', 'quantity']
- priced, unnamed: $10.0 keys=['cartQuantity', 'cartUnit', 'cbdPips', 'deal', 'dealId', 'displayQuantity', 'externalKey', 'id', 'medical', 'normalizedQuantityLabel', 'offers', 'price', 'pricePerUnit', 'quantity']
- paths: pageProps.menuData.availableFilters[].values[].badge, pageProps.menuData.availableFilters[].values[].chip, pageProps.menuData.availableFilters[].values[].count, pageProps.menuData.availableFilters[].values[].label, pageProps.menuData.availableFilters[].values[].sortOrder, pageProps.menuData.availableFilters[].values[].type, pageProps.menuData.availableFilters[].values[].value, pageProps.menuData.availableFilters[].label, pageProps.menuData.availableFilters[].name, pageProps.menuData.availableFilters[].showCount, pageProps.menuData.availableFilters[].sortOrder, pageProps.menuData.availableFilters[].type

## nevadamade — blocked before the menu loaded (HTTP 403)
- page: https://nevadamademarijuana.com/products
- json payloads: 0 (hosts: none)

## oasis — JSON captured holds no menu data (wrong URL, or menu loads elsewhere)
- page: https://oasiscannabis.com/products
- json payloads: 7 (hosts: {'otlp-http-production.shopifysvc.com': 6, 'oasiscannabis.com': 1})

## planet13 — blocked before the menu loaded (HTTP 403)
- page: https://planet13lasvegas.com/products
- json payloads: 0 (hosts: none)

## reef — JSON captured holds no menu data (wrong URL, or menu loads elsewhere)
- page: https://reefdispensaries.com/products
- json payloads: 1 (hosts: {'curaleaf.com': 1})

## rise — blocked before the menu loaded (HTTP 403)
- page: https://risecannabis.com/products
- json payloads: 0 (hosts: none)

## sanctuary — blocked before the menu loaded (HTTP 404)
- page: https://sanctuarynv.com/products
- json payloads: 0 (hosts: none)

## shango — blocked before the menu loaded (HTTP 404)
- page: https://goshango.com/deals
- json payloads: 0 (hosts: none)

## silversage — blocked before the menu loaded (HTTP 403)
- page: https://www.sswlv.com/products
- json payloads: 0 (hosts: none)

## silverstate — blocked before the menu loaded (HTTP 404)
- page: https://silverstaterelief.com/deals
- json payloads: 0 (hosts: none)

## thesource — JSON captured holds no menu data (wrong URL, or menu loads elsewhere)
- page: https://www.thesourcenv.com/deals
- json payloads: 43 (hosts: {'browser-intake-datadoghq.com': 7, 'www.thesourcenv.com': 1})

## thrive — JSON captured holds no menu data (wrong URL, or menu loads elsewhere)
- page: https://thrivenevada.com/deals
- json payloads: 1 (hosts: {'zt6taxfu2g.execute-api.us-west-1.amazonaws.com': 1})

## treeoflife — page failed to load
- page: https://treeoflifedispensary.com/products
- json payloads: 0 (hosts: none)
- error: Error: Page.goto: net::ERR_CONNECTION_CLOSED at https://treeoflifedispensary.com/products
Call log:
  - navigating to "https://treeoflifedispensary.com/products", waiting until "domcontentloaded"


## wm_dispos — named things present but no price the parser recognizes -- PARSER GAP
- page: https://weedmaps.com/dispensaries/in/united-states/nevada/las-vegas
- json payloads: 40 (hosts: {'browser-intake-datadoghq.com': 6, 'api-g.weedmaps.com': 1, 'sdk.iad-03.braze.com': 1})
- named, unpriced: 'Vape pens' keys=['avatar_image_url', 'name', 'slug', 'subcategories', 'total_products_count', 'uuid']
- named, unpriced: 'Disposable' keys=['avatar_image_url', 'name', 'slug', 'subcategories', 'total_products_count', 'uuid']
- named, unpriced: 'Cartridge' keys=['avatar_image_url', 'name', 'slug', 'subcategories', 'total_products_count', 'uuid']
- named, unpriced: 'Pods' keys=['avatar_image_url', 'name', 'slug', 'subcategories', 'total_products_count', 'uuid']
- paths: data.facets.categories[].subcategories[].total_products_count, data.facets.client_categories[].subcategories[].total_products_count, data.facets.tag_groups[].tags[].total_products_count, data.facets.categories[].total_products_count, data.facets.price_weights.gram[].units, data.facets.price_weights.gram[].total_products_count, data.facets.price_weights.gram[].label, data.facets.price_weights.gram[].product_count_storefront, data.facets.price_weights.gram[].product_count_delivery, data.facets.client_categories[].total_products_count, data.facets.price_weights.ounce[].units, data.facets.price_weights.ounce[].total_products_count

## zenleaf — 1154 product-shaped nodes present -- parser should have caught these
- page: https://zenleafdispensaries.com/menu
- json payloads: 12 (hosts: {'zenleafdispensaries.com': 4, 'data.zenleafdispensaries.com': 4})
- product-shaped nodes: 1154
- named, unpriced: 'Eastern Time (ET)' keys=['date', 'day', 'name', 'time', 'timezone', 'tomorrow']
- named, unpriced: 'Mountain Time (MT)' keys=['date', 'day', 'name', 'time', 'timezone', 'tomorrow']
- named, unpriced: 'Central Time (CT)' keys=['date', 'day', 'name', 'time', 'timezone', 'tomorrow']
- named, unpriced: 'Pacific Time (PT)' keys=['date', 'day', 'name', 'time', 'timezone', 'tomorrow']
- paths: products[].id, products[].name, products[].category, products[].category.id, products[].category.name, products[].category.canonicalName, products[].subcategory, products[].subcategory.id, products[].subcategory.name, products[].subcategory.canonicalName, products[].images, products[].brand
