# Why each store produced no offers

## beyondhello — no age gate found and no JSON fetched -- menu is server-rendered, or the page is a shell
- page: https://beyond-hello.com/shop
- json payloads: 0 (hosts: none)
- urls tried: 6
    - https://beyond-hello.com/menu -> HTTP 404
    - https://beyond-hello.com/shop -> no age gate found and no JSON fetched -- menu is server-rend
    - https://beyond-hello.com/order-online -> HTTP 404
    - https://beyond-hello.com/specials -> no age gate found and no JSON fetched -- menu is server-rend
    - https://beyond-hello.com/deals -> blocked before the menu loaded (near-empty document)
    - https://beyond-hello.com/products -> blocked before the menu loaded (near-empty document)

## cookies — page failed to load
- page: https://cookies.co/menu
- json payloads: 0 (hosts: none)
- error: Error: Page.goto: net::ERR_CERT_DATE_INVALID at https://cookies.co/menu
Call log:
  - navigating to "https://cookies.co/menu", waiting until "domcontentloaded"

- urls tried: 6
    - https://cookies.co/menu -> page failed to load
    - https://cookies.co/shop -> page failed to load
    - https://cookies.co/order-online -> page failed to load
    - https://cookies.co/specials -> page failed to load
    - https://cookies.co/deals -> page failed to load
    - https://cookies.co/products -> page failed to load

## cultivate — named things present but no price the parser recognizes -- PARSER GAP
- page: https://cultivatelv.com/online-menu/
- json payloads: 12 (hosts: {'lab.alpineiq.com': 5, 'api.iheartjane.com': 3})
- named, unpriced: 'Cultivate Dispensary - Las Vegas' keys=['address', 'aeropay_integration', 'allow_future_day_ordering', 'allow_off_hours_ordering', 'analytics_integration', 'automatic_crm_redemption', 'avg_response_time', 'birth_date_required', 'boost_menu_url', 'business_paperwork', 'canpay_enabled', 'canpay_v2remotepay_enabled', 'carousel_banner', 'cart_limit_policy']
- named, unpriced: 'Nevada Purchase Limits' keys=['cart_limit_rules', 'id', 'name']
- named, unpriced: 'Daily Deals' keys=['display_name', 'enabled', 'id', 'menu_row_type', 'row_type', 'rules']
- named, unpriced: 'Best Selling' keys=['display_name', 'enabled', 'id', 'menu_row_type', 'row_type', 'rules']
- urls tried: 6
    - https://cultivatelv.com/deals -> named things present but no price the parser recognizes -- P
    - https://cultivatelv.com/online-menu/ -> named things present but no price the parser recognizes -- P
    - https://cultivatelv.com/online-menu-durango/ -> named things present but no price the parser recognizes -- P
    - https://cultivatelv.com/menu -> age gate cleared and page reloaded, but still no JSON -- men
    - https://cultivatelv.com/shop -> HTTP 404
    - https://cultivatelv.com/order-online -> HTTP 404
- paths: store.custom_row_settings[].menu_row_type, store.store_taxes[].apply_to_discounted_price, store.store_taxes[].apply_to_non_cannabis_items, store.boost_menu_url, store.cart_limit_policy.cart_limit_rules[].product_group_name, store.cart_limit_policy.cart_limit_rules[].product_types, store.cart_limit_policy.cart_limit_rules[].product_types[].id, store.cart_limit_policy.cart_limit_rules[].product_types[].cart_limit_rule_product_type_id, store.cart_limit_policy.cart_limit_rules[].product_types[].product_subtype, store.cart_limit_policy.cart_limit_rules[].product_types[].product_type, store.current_jane_menu_url, store.custom_product_type_labels

## curaleaf — JSON captured holds no menu data (wrong URL, or menu loads elsewhere)
- page: https://curaleaf.com/menu
- json payloads: 1 (hosts: {'curaleaf.com': 1})
- urls tried: 6
    - https://curaleaf.com/menu -> JSON captured holds no menu data (wrong URL, or menu loads e
    - https://curaleaf.com/shop -> JSON captured holds no menu data (wrong URL, or menu loads e
    - https://curaleaf.com/order-online -> JSON captured holds no menu data (wrong URL, or menu loads e
    - https://curaleaf.com/specials -> JSON captured holds no menu data (wrong URL, or menu loads e
    - https://curaleaf.com/deals -> JSON captured holds no menu data (wrong URL, or menu loads e
    - https://curaleaf.com/products -> JSON captured holds no menu data (wrong URL, or menu loads e

## exhale — page failed to load
- page: https://exhalenv.com/menu
- json payloads: 0 (hosts: none)
- error: Error: Page.goto: net::ERR_NAME_NOT_RESOLVED at https://exhalenv.com/menu
Call log:
  - navigating to "https://exhalenv.com/menu", waiting until "domcontentloaded"

- urls tried: 6
    - https://exhalenv.com/menu -> page failed to load
    - https://exhalenv.com/shop -> page failed to load
    - https://exhalenv.com/order-online -> page failed to load
    - https://exhalenv.com/specials -> page failed to load
    - https://exhalenv.com/deals -> page failed to load
    - https://exhalenv.com/products -> page failed to load

## greenlight — JSON captured holds no menu data (wrong URL, or menu loads elsewhere)
- page: https://greenlightdispensary.com/specials
- json payloads: 6 (hosts: {'script.crazyegg.com': 2, 'thegreenlightdispensary.info': 1, 'cdn.acsbapp.com': 1, 'tags.srv.stackadapt.com': 1, 'greenlightdispensary.com': 1})
- urls tried: 6
    - https://greenlightdispensary.com/menu -> HTTP 404
    - https://greenlightdispensary.com/shop -> HTTP 404
    - https://greenlightdispensary.com/order-online -> HTTP 404
    - https://greenlightdispensary.com/specials -> JSON captured holds no menu data (wrong URL, or menu loads e
    - https://greenlightdispensary.com/deals -> HTTP 404
    - https://greenlightdispensary.com/products -> HTTP 404
- paths: widgetSettings.statementVariant

## inyo — named things present but no price the parser recognizes -- PARSER GAP
- page: https://inyolasvegas.com/menu
- json payloads: 18 (hosts: {'api.nevada.getcarrot.io': 7, 'sa.searchatlas.com': 1})
- named, unpriced: 'S. Maryland Pkwy' keys=['addressLine1', 'addressLine2', 'companyId', 'enabled', 'id', 'imageUrl', 'name', 'sort', 'timeZoneId']
- named, unpriced: 'S. Maryland Pkwy' keys=['addressLine1', 'addressLine2', 'companyId', 'enabled', 'id', 'imageUrl', 'name', 'sort', 'timeZoneId']
- paths: refresh_product_recommendations, redemptionByProduct, pickup:min_price, minimum_item_price, surfside:product_list_zone_id, system:in_store_menu_dark_mode, system:in_store_menu_queue_image, system:in_store_menu_rotation, system:in_store_menu_background

## jardin — blocked before the menu loaded (HTTP 404)
- page: https://jardincannabis.com/menu
- json payloads: 0 (hosts: none)
- urls tried: 6
    - https://jardincannabis.com/menu -> HTTP 404
    - https://jardincannabis.com/shop -> HTTP 404
    - https://jardincannabis.com/order-online -> HTTP 404
    - https://jardincannabis.com/specials -> HTTP 404
    - https://jardincannabis.com/deals -> HTTP 404
    - https://jardincannabis.com/products -> HTTP 404

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

## nevadamade — no age gate found and no JSON fetched -- menu is server-rendered, or the page is a shell
- page: https://nevadamademarijuana.com/specials
- json payloads: 0 (hosts: none)
- urls tried: 6
    - https://nevadamademarijuana.com/menu -> blocked before the menu loaded (near-empty document)
    - https://nevadamademarijuana.com/shop -> blocked before the menu loaded (near-empty document)
    - https://nevadamademarijuana.com/order-online -> HTTP 403
    - https://nevadamademarijuana.com/specials -> no age gate found and no JSON fetched -- menu is server-rend
    - https://nevadamademarijuana.com/deals -> HTTP 403
    - https://nevadamademarijuana.com/products -> HTTP 403

## oasis — JSON captured holds no menu data (wrong URL, or menu loads elsewhere)
- page: https://oasiscannabis.com/menu
- json payloads: 7 (hosts: {'otlp-http-production.shopifysvc.com': 6, 'oasiscannabis.com': 1})
- urls tried: 6
    - https://oasiscannabis.com/menu -> HTTP 404
    - https://oasiscannabis.com/shop -> JSON captured holds no menu data (wrong URL, or menu loads e
    - https://oasiscannabis.com/order-online -> HTTP 404
    - https://oasiscannabis.com/specials -> HTTP 404
    - https://oasiscannabis.com/deals -> HTTP 404
    - https://oasiscannabis.com/products -> JSON captured holds no menu data (wrong URL, or menu loads e

## planet13 — blocked before the menu loaded (HTTP 403)
- page: https://planet13lasvegas.com/menu
- json payloads: 0 (hosts: none)
- urls tried: 6
    - https://planet13lasvegas.com/menu -> HTTP 403
    - https://planet13lasvegas.com/shop -> HTTP 403
    - https://planet13lasvegas.com/order-online -> HTTP 403
    - https://planet13lasvegas.com/specials -> HTTP 403
    - https://planet13lasvegas.com/deals -> HTTP 403
    - https://planet13lasvegas.com/products -> HTTP 403

## reef — JSON captured holds no menu data (wrong URL, or menu loads elsewhere)
- page: https://reefdispensaries.com/menu
- json payloads: 1 (hosts: {'curaleaf.com': 1})
- urls tried: 6
    - https://reefdispensaries.com/menu -> JSON captured holds no menu data (wrong URL, or menu loads e
    - https://reefdispensaries.com/shop -> JSON captured holds no menu data (wrong URL, or menu loads e
    - https://reefdispensaries.com/order-online -> JSON captured holds no menu data (wrong URL, or menu loads e
    - https://reefdispensaries.com/specials -> JSON captured holds no menu data (wrong URL, or menu loads e
    - https://reefdispensaries.com/deals -> JSON captured holds no menu data (wrong URL, or menu loads e
    - https://reefdispensaries.com/products -> JSON captured holds no menu data (wrong URL, or menu loads e

## rise — blocked before the menu loaded (Cloudflare challenge)
- page: https://risecannabis.com/menu
- json payloads: 0 (hosts: none)
- urls tried: 6
    - https://risecannabis.com/menu -> blocked before the menu loaded (Cloudflare challenge)
    - https://risecannabis.com/shop -> HTTP 403
    - https://risecannabis.com/order-online -> HTTP 403
    - https://risecannabis.com/specials -> HTTP 403
    - https://risecannabis.com/deals -> HTTP 403
    - https://risecannabis.com/products -> HTTP 403

## sanctuary — blocked before the menu loaded (HTTP 404)
- page: https://sanctuarynv.com/menu
- json payloads: 0 (hosts: none)
- urls tried: 6
    - https://sanctuarynv.com/menu -> HTTP 404
    - https://sanctuarynv.com/shop -> HTTP 404
    - https://sanctuarynv.com/order-online -> HTTP 404
    - https://sanctuarynv.com/specials -> HTTP 404
    - https://sanctuarynv.com/deals -> HTTP 404
    - https://sanctuarynv.com/products -> HTTP 404

## shango — no age gate found and no JSON fetched -- menu is server-rendered, or the page is a shell
- page: https://goshango.com/order-online
- json payloads: 0 (hosts: none)
- urls tried: 6
    - https://goshango.com/order -> HTTP 404
    - https://goshango.com/menu -> HTTP 404
    - https://goshango.com/shop -> HTTP 404
    - https://goshango.com/order-online -> no age gate found and no JSON fetched -- menu is server-rend
    - https://goshango.com/specials -> HTTP 404
    - https://goshango.com/deals -> HTTP 404

## silversage — no age gate found and no JSON fetched -- menu is server-rendered, or the page is a shell
- page: https://www.sswlv.com/menu
- json payloads: 0 (hosts: none)
- urls tried: 6
    - https://www.sswlv.com/menu -> no age gate found and no JSON fetched -- menu is server-rend
    - https://www.sswlv.com/shop -> HTTP 403
    - https://www.sswlv.com/order-online -> HTTP 403
    - https://www.sswlv.com/specials -> HTTP 403
    - https://www.sswlv.com/deals -> HTTP 403
    - https://www.sswlv.com/products -> HTTP 403

## silverstate — JSON captured holds no menu data (wrong URL, or menu loads elsewhere)
- page: https://silverstaterelief.com/menu
- json payloads: 58 (hosts: {'browser-intake-datadoghq.com': 8})
- urls tried: 6
    - https://silverstaterelief.com/menu -> JSON captured holds no menu data (wrong URL, or menu loads e
    - https://silverstaterelief.com/shop -> HTTP 404
    - https://silverstaterelief.com/order-online -> HTTP 404
    - https://silverstaterelief.com/specials -> HTTP 404
    - https://silverstaterelief.com/deals -> HTTP 404
    - https://silverstaterelief.com/products -> HTTP 404

## thesource — named things present but no price the parser recognizes -- PARSER GAP
- page: https://www.thesourcenv.com/shop
- json payloads: 8 (hosts: {'lab.alpineiq.com': 6, 'ada.skynettechnologies.us': 2})
- named, unpriced: 'The Source Jane' keys=['connectionId', 'inventoryProvider', 'menuProvider', 'name']
- urls tried: 6
    - https://www.thesourcenv.com/menu -> JSON captured holds no menu data (wrong URL, or menu loads e
    - https://www.thesourcenv.com/shop -> HTTP 404
    - https://www.thesourcenv.com/order-online -> HTTP 404
    - https://www.thesourcenv.com/specials -> named things present but no price the parser recognizes -- P
    - https://www.thesourcenv.com/deals -> JSON captured holds no menu data (wrong URL, or menu loads e
    - https://www.thesourcenv.com/menu/api/footer.data?_routes=routes%2Fapi.footer -> JSON captured holds no menu data (wrong URL, or menu loads e
- paths: data.ecomLocations[].subEcomLocations[].menuType, data.ecomLocations[].subEcomLocations[].ecomMenuProvider, data.ecomLocations[].ecomMenuProviders, data.ecomMenuProviders, data.menuType, data.recommendationSettings.screenSettings.price, data.recommendationSettings.screenSettings.price.enabled, data.recommendationSettings.screenSettings.price.required, data.recommendationSettings.screenSettings.price.edibleEnabled, data.recommendationSettings.screenSettings.price.edibleRequired, data.reviewSettings.screenSettings.productList, data.screenSettings.productDetails

## thrive — JSON captured holds no menu data (wrong URL, or menu loads elsewhere)
- page: https://thrivenevada.com/menu
- json payloads: 1 (hosts: {'zt6taxfu2g.execute-api.us-west-1.amazonaws.com': 1})
- urls tried: 6
    - https://thrivenevada.com/menu -> HTTP 404
    - https://zt6taxfu2g.execute-api.us-west-1.amazonaws.com/prod/retail/all?retailURL -> HTTP 403
    - https://thrivenevada.com/shop -> HTTP 404
    - https://thrivenevada.com/order-online -> HTTP 404
    - https://thrivenevada.com/specials -> HTTP 404
    - https://thrivenevada.com/deals -> HTTP 404

## treeoflife — page failed to load
- page: https://treeoflifedispensary.com/menu
- json payloads: 0 (hosts: none)
- error: Error: Page.goto: net::ERR_CONNECTION_CLOSED at https://treeoflifedispensary.com/menu
Call log:
  - navigating to "https://treeoflifedispensary.com/menu", waiting until "domcontentloaded"

- urls tried: 6
    - https://treeoflifedispensary.com/menu -> page failed to load
    - https://treeoflifedispensary.com/shop -> page failed to load
    - https://treeoflifedispensary.com/order-online -> page failed to load
    - https://treeoflifedispensary.com/specials -> page failed to load
    - https://treeoflifedispensary.com/deals -> page failed to load
    - https://treeoflifedispensary.com/products -> page failed to load

## wm_dispos — named things present but no price the parser recognizes -- PARSER GAP
- page: https://weedmaps.com/dispensaries/in/united-states/nevada/las-vegas
- json payloads: 41 (hosts: {'browser-intake-datadoghq.com': 5, 'sdk.iad-03.braze.com': 2, 'api-g.weedmaps.com': 1})
- named, unpriced: 'Vape pens' keys=['avatar_image_url', 'name', 'slug', 'subcategories', 'total_products_count', 'uuid']
- named, unpriced: 'Disposable' keys=['avatar_image_url', 'name', 'slug', 'subcategories', 'total_products_count', 'uuid']
- named, unpriced: 'Cartridge' keys=['avatar_image_url', 'name', 'slug', 'subcategories', 'total_products_count', 'uuid']
- named, unpriced: 'Pods' keys=['avatar_image_url', 'name', 'slug', 'subcategories', 'total_products_count', 'uuid']
- paths: data.facets.categories[].subcategories[].total_products_count, data.facets.client_categories[].subcategories[].total_products_count, data.facets.tag_groups[].tags[].total_products_count, data.facets.categories[].total_products_count, data.facets.price_weights.gram[].units, data.facets.price_weights.gram[].total_products_count, data.facets.price_weights.gram[].label, data.facets.price_weights.gram[].product_count_storefront, data.facets.price_weights.gram[].product_count_delivery, data.facets.client_categories[].total_products_count, data.facets.price_weights.ounce[].units, data.facets.price_weights.ounce[].total_products_count

## zenleaf — 811 product-shaped nodes present -- parser should have caught these
- page: https://zenleafdispensaries.com/menu
- json payloads: 12 (hosts: {'zenleafdispensaries.com': 4, 'data.zenleafdispensaries.com': 4})
- product-shaped nodes: 811
- named, unpriced: 'Abington' keys=['address_1', 'address_2', 'bodegaStore', 'city', 'hours', 'lat', 'lng', 'locationId', 'location_status', 'medicalStoreId', 'phoneNumberOverride', 'post_id', 'post_title', 'recreationalStoreId']
- named, unpriced: 'Altoona' keys=['address_1', 'address_2', 'bodegaStore', 'city', 'hours', 'lat', 'lng', 'locationId', 'location_status', 'medicalStoreId', 'phoneNumberOverride', 'post_id', 'post_title', 'recreationalStoreId']
- named, unpriced: 'Antwerp' keys=['address_1', 'address_2', 'bodegaStore', 'city', 'hours', 'lat', 'lng', 'locationId', 'location_status', 'medicalStoreId', 'phoneNumberOverride', 'post_id', 'post_title', 'recreationalStoreId']
- named, unpriced: 'Arcadia' keys=['address_1', 'address_2', 'bodegaStore', 'city', 'hours', 'lat', 'lng', 'locationId', 'location_status', 'medicalStoreId', 'phoneNumberOverride', 'post_id', 'post_title', 'recreationalStoreId']
- paths: products[].id, products[].name, products[].category, products[].category.id, products[].category.name, products[].category.canonicalName, products[].subcategory, products[].subcategory.id, products[].subcategory.name, products[].subcategory.canonicalName, products[].images, products[].brand
