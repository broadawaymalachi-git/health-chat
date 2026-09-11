# Why each store produced no offers

## beyondhello — named things present but no price the parser recognizes -- PARSER GAP
- page: https://www.iheartjane.com/embed/stores/4536/menu/vapes
- json payloads: 10 (hosts: {'www.iheartjane.com': 4, 'api.iheartjane.com': 4})
- named, unpriced: 'BEYOND / HELLO - Alexandria (Pickup Menu)' keys=['address', 'aeropay_integration', 'allow_future_day_ordering', 'allow_off_hours_ordering', 'analytics_integration', 'automatic_crm_redemption', 'avg_response_time', 'birth_date_required', 'boost_menu_url', 'business_paperwork', 'canpay_enabled', 'canpay_v2remotepay_enabled', 'carousel_banner', 'cart_limit_policy']
- named, unpriced: 'Best Sellers' keys=['display_name', 'enabled', 'id', 'menu_row_type', 'row_type', 'rules']
- named, unpriced: 'Flower' keys=['display_name', 'enabled', 'id', 'menu_row_type', 'row_type', 'rules']
- named, unpriced: 'Edible' keys=['display_name', 'enabled', 'id', 'menu_row_type', 'row_type', 'rules']
- urls tried: 6
    - https://beyond-hello.com/menu -> HTTP 404
    - https://beyond-hello.com/shop -> named things present but no price the parser recognizes -- P
    - https://www.iheartjane.com/embed/stores/4536/menu -> named things present but no price the parser recognizes -- P
    - https://www.iheartjane.com/embed/stores/4536/menu/vapes -> named things present but no price the parser recognizes -- P
    - https://beyond-hello.com/menus/?_by_state=virginia -> HTTP 404
    - https://vfm4x0n23a-dsn.algolia.net/1/indexes/menu-products-production/query -> HTTP 403
- paths: store.custom_row_settings[].menu_row_type, store.boost_menu_url, store.current_jane_menu_url, store.custom_product_type_labels, store.custom_product_type_labels.gear:Paraphernalia, store.custom_product_type_labels.sale, store.custom_product_type_labels.best_selling, store.custom_product_type_labels.specials, store.custom_product_type_labels.magic_row, store.custom_product_type_labels.buy_again_row, store.custom_product_type_labels.Back in stock‼️, store.custom_product_type_labels.Flower

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
- page: https://www.iheartjane.com/embed/stores/2602/menu
- json payloads: 17 (hosts: {'api.iheartjane.com': 5, 'www.iheartjane.com': 3})
- named, unpriced: 'Culti | M&M 8ths (14g) for $70 OTD' keys=['conditions', 'created_at', 'custom_badge', 'description', 'discount_amount', 'discount_dollar_amount', 'discount_percent', 'discount_target_price', 'discount_type', 'hidden_from_page', 'hidden_from_row', 'id', 'photo', 'reservation_modes']
- named, unpriced: 'Bounti/Kanha | B1G1 (Exclusions Apply)' keys=['conditions', 'created_at', 'custom_badge', 'description', 'discount_amount', 'discount_dollar_amount', 'discount_percent', 'discount_target_price', 'discount_type', 'hidden_from_page', 'hidden_from_row', 'id', 'photo', 'reservation_modes']
- named, unpriced: 'Stiiizy | 30% Off (Exclusions Apply)' keys=['conditions', 'created_at', 'custom_badge', 'description', 'discount_amount', 'discount_dollar_amount', 'discount_percent', 'discount_target_price', 'discount_type', 'hidden_from_page', 'hidden_from_row', 'id', 'photo', 'reservation_modes']
- named, unpriced: 'Rove | 40% Off (EXCLUDES RTUs)' keys=['conditions', 'created_at', 'custom_badge', 'description', 'discount_amount', 'discount_dollar_amount', 'discount_percent', 'discount_target_price', 'discount_type', 'hidden_from_page', 'hidden_from_row', 'id', 'photo', 'reservation_modes']
- urls tried: 6
    - https://cultivatelv.com/deals -> named things present but no price the parser recognizes -- P
    - https://cultivatelv.com/online-menu/ -> named things present but no price the parser recognizes -- P
    - https://www.iheartjane.com/embed/stores/2602/menu -> named things present but no price the parser recognizes -- P
    - https://www.iheartjane.com/embed/stores/2602/menu/vapes -> named things present but no price the parser recognizes -- P
    - https://cultivatelv.com/online-menu-durango/ -> named things present but no price the parser recognizes -- P
    - https://www.iheartjane.com/embed/stores/5942/menu -> named things present but no price the parser recognizes -- P
- paths: store.custom_row_settings[].menu_row_type, store.custom_row_settings[].rules.rule_sets[].all_products, specials[].discount_target_price, specials[].conditions.product.kinds[].kind, store.store_taxes[].apply_to_discounted_price, store.store_taxes[].apply_to_non_cannabis_items, specials[].conditions.product, specials[].conditions.bundle.independent.threshold_number_of_items_in_cart, specials[].conditions.bundle.dependent.max_number_of_discounted_products, specials[].conditions.bundle.settings.allow_discounts_on_required_products, specials[].conditions.bundle.settings.exclude_product_specials_from_bundle_qualifiers, specials[].conditions.bundle.settings.copy_conditions_for_discounted_products

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

## euphoria — 89 product-shaped nodes present -- parser should have caught these
- page: https://euphoriawellnessnv.com/menu
- json payloads: 9 (hosts: {'web-ui-prime.sweedpos.com': 7, 'sentry.kube-prod.sweedpos.com': 1})
- product-shaped nodes: 89
- named, unpriced: 'Euphoria Wellness - Las Vegas' keys=['amenities', 'contacts', 'dealerId', 'deliveryPromos', 'deliveryZones', 'id', 'images', 'instance', 'isCaregiverOrdersEnabled', 'isMock', 'location', 'name', 'routeName', 'saleTypes']
- named, unpriced: 'Store hours' keys=['name', 'schedules', 'type']
- named, unpriced: 'In-store pickup' keys=['name', 'schedules', 'type']
- named, unpriced: 'Curbside pickup' keys=['name', 'schedules', 'type']
- paths: [].products[].strain.terpenes[].name, [].products[].strain.terpenes[].canonicalName, [].products[].id, [].products[].name, [].products[].description, [].products[].category, [].products[].category.id, [].products[].category.name, [].products[].category.canonicalName, [].products[].subcategory, [].products[].images, [].products[].brand

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
- json payloads: 11 (hosts: {'script.crazyegg.com': 4, 'cdn.acsbapp.com': 1, 'tags.srv.stackadapt.com': 1, 'thegreenlightdispensary.info': 1, 'greenlightdispensary.com': 1})
- urls tried: 6
    - https://greenlightdispensary.com/menu -> HTTP 404
    - https://greenlightdispensary.com/shop -> HTTP 404
    - https://greenlightdispensary.com/order-online -> HTTP 404
    - https://greenlightdispensary.com/specials -> JSON captured holds no menu data (wrong URL, or menu loads e
    - https://greenlightdispensary.com/deals -> HTTP 404
    - https://greenlightdispensary.com/products -> HTTP 404
- paths: widgetSettings.statementVariant

## greennv — named things present but no price the parser recognizes -- PARSER GAP
- page: https://greennv.com/menu
- json payloads: 3 (hosts: {'events.usermaven.com': 2, 'greennv.com': 1})
- named, unpriced: 'Green Dispensary North' keys=['address', 'addressObject', 'coordinates', 'fulfillmentOptions', 'hours', 'id', 'image', 'name', 'openedAt', 'phone', 'serviceOptions', 'storefrontSlug']
- named, unpriced: 'Green Dispensary Hualapai' keys=['address', 'addressObject', 'coordinates', 'fulfillmentOptions', 'hours', 'id', 'image', 'name', 'openedAt', 'phone', 'serviceOptions', 'storefrontSlug']
- named, unpriced: 'Green Dispensary Henderson' keys=['address', 'addressObject', 'coordinates', 'fulfillmentOptions', 'hours', 'id', 'image', 'name', 'openedAt', 'phone', 'serviceOptions', 'storefrontSlug']
- named, unpriced: 'Green Dispensary Rainbow' keys=['address', 'addressObject', 'coordinates', 'fulfillmentOptions', 'hours', 'id', 'image', 'name', 'openedAt', 'phone', 'serviceOptions', 'storefrontSlug']
- urls tried: 6
    - https://greennv.com/menu -> named things present but no price the parser recognizes -- P
    - https://greennv.com/shop -> named things present but no price the parser recognizes -- P
    - https://greennv.com/order-online -> HTTP 404
    - https://greennv.com/specials -> named things present but no price the parser recognizes -- P
    - https://greennv.com/deals -> named things present but no price the parser recognizes -- P
    - https://greennv.com/products -> named things present but no price the parser recognizes -- P

## inyo — named things present but no price the parser recognizes -- PARSER GAP
- page: https://inyolasvegas.com/menu
- json payloads: 18 (hosts: {'api.nevada.getcarrot.io': 8})
- named, unpriced: 'S. Maryland Pkwy' keys=['addressLine1', 'addressLine2', 'companyId', 'enabled', 'id', 'imageUrl', 'name', 'sort', 'timeZoneId']
- named, unpriced: 'S. Maryland Pkwy' keys=['addressLine1', 'addressLine2', 'companyId', 'enabled', 'id', 'imageUrl', 'name', 'sort', 'timeZoneId']
- named, unpriced: 'CONES (LIL LEAN)' keys=['batchId', 'batchName', 'brand', 'cacheTimestamp', 'carrotSubcategory', 'cashPriceRange', 'categoryName', 'categorySlug', 'description', 'descriptionAndroid', 'descriptionIos', 'effectTags', 'embedding', 'id']
- named, unpriced: 'INTEGRA BOOST 2 WAY HUMIDITY CONTROL PACK' keys=['batchId', 'batchName', 'brand', 'cacheTimestamp', 'carrotSubcategory', 'cashPriceRange', 'categoryName', 'categorySlug', 'description', 'descriptionAndroid', 'descriptionIos', 'effectTags', 'embedding', 'id']
- paths: results[].hits[].document.cashPriceRange, results[].hits[].document.option1Price, results[].hits[].document.unitWeight, results[].hits[].document.weights, pickup:min_price, minimum_item_price, surfside:product_list_zone_id, system:in_store_menu_dark_mode, system:in_store_menu_queue_image, system:in_store_menu_rotation, system:in_store_menu_background, refresh_product_recommendations

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

## nevadamade — blocked before the menu loaded (HTTP 403)
- page: https://nevadamademarijuana.com/menu
- json payloads: 0 (hosts: none)
- urls tried: 6
    - https://nevadamademarijuana.com/menu -> HTTP 403
    - https://nevadamademarijuana.com/shop -> HTTP 403
    - https://nevadamademarijuana.com/order-online -> HTTP 403
    - https://nevadamademarijuana.com/specials -> HTTP 403
    - https://nevadamademarijuana.com/deals -> HTTP 403
    - https://nevadamademarijuana.com/products -> HTTP 403

## oasis — named things present but no price the parser recognizes -- PARSER GAP
- page: https://oasiscannabis.com/menu
- json payloads: 18 (hosts: {'otlp-http-production.shopifysvc.com': 6, 'sentry.kube-prod.sweedpos.com': 1, 'web-ui-prime.sweedpos.com': 1})
- named, unpriced: 'Oasis Cannabis Dispensary' keys=['amenities', 'contacts', 'dealerId', 'deliveryPromos', 'deliveryZones', 'id', 'images', 'instance', 'isCaregiverOrdersEnabled', 'isMock', 'location', 'name', 'routeName', 'saleTypes']
- named, unpriced: 'Store hours' keys=['name', 'schedules', 'type']
- named, unpriced: 'In-store pickup' keys=['name', 'schedules', 'type']
- named, unpriced: 'Curbside pickup' keys=['name', 'schedules', 'type']
- paths: storeInfo.deliveryZones[].freeShippingPriceThreshold

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

## silversage — blocked before the menu loaded (HTTP 403)
- page: https://www.sswlv.com/menu
- json payloads: 0 (hosts: none)
- urls tried: 6
    - https://www.sswlv.com/menu -> HTTP 403
    - https://www.sswlv.com/shop -> HTTP 403
    - https://www.sswlv.com/order-online -> HTTP 403
    - https://www.sswlv.com/specials -> HTTP 403
    - https://www.sswlv.com/deals -> HTTP 403
    - https://www.sswlv.com/products -> HTTP 403

## silverstate — JSON captured holds no menu data (wrong URL, or menu loads elsewhere)
- page: https://silverstaterelief.com/menu
- json payloads: 64 (hosts: {'browser-intake-datadoghq.com': 8})
- urls tried: 6
    - https://silverstaterelief.com/menu -> JSON captured holds no menu data (wrong URL, or menu loads e
    - https://silverstaterelief.com/menu/api/menu-top-row?searchFilter=&storeId=6020&e -> JSON captured holds no menu data (wrong URL, or menu loads e
    - https://silverstaterelief.com/menu/vape.data?_routes=routes%2F_menu.%28%24storeS -> JSON captured holds no menu data (wrong URL, or menu loads e
    - https://silverstaterelief.com/shop -> HTTP 404
    - https://silverstaterelief.com/order-online -> HTTP 404
    - https://silverstaterelief.com/specials -> HTTP 404

## thedispensary — JSON captured holds no menu data (wrong URL, or menu loads elsewhere)
- page: https://thedispensarynv.com/shop
- json payloads: 1 (hosts: {'script.crazyegg.com': 1})
- urls tried: 6
    - https://thedispensarynv.com/shop -> JSON captured holds no menu data (wrong URL, or menu loads e
    - https://thedispensarynv.com/menu -> JSON captured holds no menu data (wrong URL, or menu loads e
    - https://thedispensarynv.com/order-online -> HTTP 404
    - https://thedispensarynv.com/specials -> HTTP 404
    - https://thedispensarynv.com/deals -> JSON captured holds no menu data (wrong URL, or menu loads e
    - https://thedispensarynv.com/products -> HTTP 404

## thesource — named things present but no price the parser recognizes -- PARSER GAP
- page: https://www.thesourcenv.com/shop
- json payloads: 8 (hosts: {'lab.alpineiq.com': 6, 'ada.skynettechnologies.us': 2})
- named, unpriced: 'The Source Jane' keys=['connectionId', 'inventoryProvider', 'menuProvider', 'name']
- urls tried: 6
    - https://www.thesourcenv.com/menu -> JSON captured holds no menu data (wrong URL, or menu loads e
    - https://www.thesourcenv.com/menu/jane-gold/1687/buy-3-select-sauce-essentials-va -> JSON captured holds no menu data (wrong URL, or menu loads e
    - https://www.thesourcenv.com/shop -> HTTP 404
    - https://www.thesourcenv.com/order-online -> HTTP 404
    - https://www.thesourcenv.com/specials -> named things present but no price the parser recognizes -- P
    - https://www.thesourcenv.com/deals -> JSON captured holds no menu data (wrong URL, or menu loads e
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

## wm_deals — 20 product-shaped nodes present -- parser should have caught these
- page: https://weedmaps.com/dispensaries/euphoria-wellness
- json payloads: 51 (hosts: {'api-g.weedmaps.com': 8})
- product-shaped nodes: 20
- named, unpriced: 'Effects' keys=['name', 'tags', 'uuid']
- named, unpriced: 'Relaxed' keys=['name', 'total_menu_items_count', 'uuid']
- named, unpriced: 'Euphoric' keys=['name', 'total_menu_items_count', 'uuid']
- named, unpriced: 'Uplifted' keys=['name', 'total_menu_items_count', 'uuid']
- priced, unnamed: $55.0 keys=['amount', 'currency']
- priced, unnamed: $40.0 keys=['amount', 'currency']
- priced, unnamed: $45.0 keys=['amount', 'currency']
- urls tried: 2
    - https://weedmaps.com/deals/united-states/nevada/las-vegas -> named things present but no price the parser recognizes -- P
    - https://weedmaps.com/dispensaries/euphoria-wellness -> 20 product-shaped nodes present -- parser should have caught
- paths: data.tag_groups[].tags[].total_menu_items_count, data.facets.tag_groups[].tags[].total_products_count, data.categories[].subcategories[].total_menu_items_count, data.facets.categories[].subcategories[].total_products_count, data.facets.client_categories[].subcategories[].total_products_count, data.categories[].total_menu_items_count, data[].attributes.prices, data[].attributes.prices.price_unit, data[].attributes.prices.price_half_gram, data[].attributes.prices.price_gram, data[].attributes.prices.price_two_grams, data[].attributes.prices.price_eighth

## wm_dispos — named things present but no price the parser recognizes -- PARSER GAP
- page: https://weedmaps.com/dispensaries/in/united-states/nevada/las-vegas
- json payloads: 40 (hosts: {'browser-intake-datadoghq.com': 5, 'sdk.iad-03.braze.com': 2, 'api-g.weedmaps.com': 1})
- named, unpriced: 'Vape pens' keys=['avatar_image_url', 'name', 'slug', 'subcategories', 'total_products_count', 'uuid']
- named, unpriced: 'Disposable' keys=['avatar_image_url', 'name', 'slug', 'subcategories', 'total_products_count', 'uuid']
- named, unpriced: 'Cartridge' keys=['avatar_image_url', 'name', 'slug', 'subcategories', 'total_products_count', 'uuid']
- named, unpriced: 'Pods' keys=['avatar_image_url', 'name', 'slug', 'subcategories', 'total_products_count', 'uuid']
- paths: data.facets.categories[].subcategories[].total_products_count, data.facets.client_categories[].subcategories[].total_products_count, data.facets.tag_groups[].tags[].total_products_count, data.facets.categories[].total_products_count, data.facets.price_weights.gram[].units, data.facets.price_weights.gram[].total_products_count, data.facets.price_weights.gram[].label, data.facets.price_weights.gram[].product_count_storefront, data.facets.price_weights.gram[].product_count_delivery, data.facets.client_categories[].total_products_count, data.facets.price_weights.ounce[].units, data.facets.price_weights.ounce[].total_products_count

## zenleaf — 1131 product-shaped nodes present -- parser should have caught these
- page: https://zenleafdispensaries.com/menu
- json payloads: 12 (hosts: {'zenleafdispensaries.com': 4, 'data.zenleafdispensaries.com': 4})
- product-shaped nodes: 1131
- named, unpriced: 'Eastern Time (ET)' keys=['date', 'day', 'name', 'time', 'timezone', 'tomorrow']
- named, unpriced: 'Mountain Time (MT)' keys=['date', 'day', 'name', 'time', 'timezone', 'tomorrow']
- named, unpriced: 'Central Time (CT)' keys=['date', 'day', 'name', 'time', 'timezone', 'tomorrow']
- named, unpriced: 'Pacific Time (PT)' keys=['date', 'day', 'name', 'time', 'timezone', 'tomorrow']
- paths: products[].id, products[].name, products[].category, products[].category.id, products[].category.name, products[].category.canonicalName, products[].subcategory, products[].subcategory.id, products[].subcategory.name, products[].subcategory.canonicalName, products[].images, products[].brand
