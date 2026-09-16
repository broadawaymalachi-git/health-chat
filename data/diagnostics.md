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
- page: https://www.iheartjane.com/embed/stores/2602/menu/vapes
- json payloads: 15 (hosts: {'www.iheartjane.com': 3, 'api.iheartjane.com': 3, 'lab.alpineiq.com': 2})
- named, unpriced: 'Cultivate Dispensary - Las Vegas' keys=['address', 'aeropay_integration', 'allow_future_day_ordering', 'allow_off_hours_ordering', 'analytics_integration', 'automatic_crm_redemption', 'avg_response_time', 'birth_date_required', 'boost_menu_url', 'business_paperwork', 'canpay_enabled', 'canpay_v2remotepay_enabled', 'carousel_banner', 'cart_limit_policy']
- named, unpriced: 'Nevada Purchase Limits' keys=['cart_limit_rules', 'id', 'name']
- named, unpriced: 'Daily Deals' keys=['display_name', 'enabled', 'id', 'menu_row_type', 'row_type', 'rules']
- named, unpriced: 'Best Selling' keys=['display_name', 'enabled', 'id', 'menu_row_type', 'row_type', 'rules']
- urls tried: 6
    - https://cultivatelv.com/deals -> named things present but no price the parser recognizes -- P
    - https://cultivatelv.com/online-menu/ -> named things present but no price the parser recognizes -- P
    - https://www.iheartjane.com/embed/stores/2602/menu -> named things present but no price the parser recognizes -- P
    - https://www.iheartjane.com/embed/stores/2602/menu/vapes -> named things present but no price the parser recognizes -- P
    - https://cultivatelv.com/online-menu-durango/ -> named things present but no price the parser recognizes -- P
    - https://www.iheartjane.com/embed/stores/5942/menu -> named things present but no price the parser recognizes -- P
- paths: store.custom_row_settings[].menu_row_type, store.custom_row_settings[].rules.rule_sets[].all_products, store.store_taxes[].apply_to_discounted_price, store.store_taxes[].apply_to_non_cannabis_items, store.boost_menu_url, store.cart_limit_policy.cart_limit_rules[].product_group_name, store.cart_limit_policy.cart_limit_rules[].product_types, store.cart_limit_policy.cart_limit_rules[].product_types[].id, store.cart_limit_policy.cart_limit_rules[].product_types[].cart_limit_rule_product_type_id, store.cart_limit_policy.cart_limit_rules[].product_types[].product_subtype, store.cart_limit_policy.cart_limit_rules[].product_types[].product_type, store.current_jane_menu_url

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
- json payloads: 10 (hosts: {'web-ui-prime.sweedpos.com': 8})
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
- json payloads: 11 (hosts: {'script.crazyegg.com': 3, 'cdn.acsbapp.com': 2, 'tags.srv.stackadapt.com': 1, 'thegreenlightdispensary.info': 1, 'greenlightdispensary.com': 1})
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
- json payloads: 18 (hosts: {'api.nevada.getcarrot.io': 7, 'sa.searchatlas.com': 1})
- named, unpriced: 'S. Maryland Pkwy' keys=['addressLine1', 'addressLine2', 'companyId', 'enabled', 'id', 'imageUrl', 'name', 'sort', 'timeZoneId']
- named, unpriced: 'S. Maryland Pkwy' keys=['addressLine1', 'addressLine2', 'companyId', 'enabled', 'id', 'imageUrl', 'name', 'sort', 'timeZoneId']
- paths: pickup:min_price, minimum_item_price, surfside:product_list_zone_id, system:in_store_menu_dark_mode, system:in_store_menu_queue_image, system:in_store_menu_rotation, system:in_store_menu_background, refresh_product_recommendations, redemptionByProduct

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

## leafly_deals — 1 product-shaped nodes present -- parser should have caught these
- page: https://www.leafly.com/deals/las-vegas-nv-us
- json payloads: 3 (hosts: {'securepubads.g.doubleclick.net': 1, 'www.leafly.com': 1, 'consumer-api.leafly.com': 1})
- product-shaped nodes: 1
- named, unpriced: "5 for $35 Solaris 1g Flower Mix'n'Match" keys=['active', 'buyQuantity', 'cadence', 'daysOfWeek', 'dealSegments', 'dealTiers', 'discountAmount', 'discountLabel', 'discountType', 'dispensary', 'dispensaryTimeZone', 'endsAt', 'finePrint', 'getQuantity']
- named, unpriced: 'The Sanctuary - North Las Vegas' keys=['distanceMi', 'hasDeliveryEnabled', 'hasReservationsEnabled', 'id', 'locations', 'name', 'primaryLocation', 'slug', 'timeZone']
- named, unpriced: '5/$35 on ALL $10 Prerolls!' keys=['active', 'buyQuantity', 'cadence', 'daysOfWeek', 'dealSegments', 'dealTiers', 'discountAmount', 'discountLabel', 'discountType', 'dispensary', 'dispensaryTimeZone', 'endsAt', 'finePrint', 'getQuantity']
- named, unpriced: 'The Sanctuary - North Las Vegas' keys=['distanceMi', 'hasDeliveryEnabled', 'hasReservationsEnabled', 'id', 'locations', 'name', 'primaryLocation', 'slug', 'timeZone']
- priced, unnamed: $13.0 keys=['cartQuantity', 'cartUnit', 'cbdPips', 'deal', 'dealId', 'displayQuantity', 'externalKey', 'id', 'medical', 'normalizedQuantityLabel', 'offers', 'price', 'pricePerUnit', 'quantity']
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

## oasis — JSON captured holds no menu data (wrong URL, or menu loads elsewhere)
- page: https://oasiscannabis.com/menu
- json payloads: 19 (hosts: {'otlp-http-production.shopifysvc.com': 7, 'sentry.kube-prod.sweedpos.com': 1})

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

## shango — blocked before the menu loaded (HTTP 404)
- page: https://goshango.com/order
- json payloads: 0 (hosts: none)
- urls tried: 6
    - https://goshango.com/order -> HTTP 404
    - https://goshango.com/menu -> HTTP 404
    - https://goshango.com/shop -> HTTP 404
    - https://goshango.com/order-online -> page failed to load
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
- json payloads: 31 (hosts: {'browser-intake-datadoghq.com': 8})
- urls tried: 6
    - https://silverstaterelief.com/menu -> JSON captured holds no menu data (wrong URL, or menu loads e
    - https://silverstaterelief.com/menu/api/menu-top-row?searchFilter=&storeId=2214&e -> JSON captured holds no menu data (wrong URL, or menu loads e
    - https://silverstaterelief.com/shop -> HTTP 404
    - https://silverstaterelief.com/order-online -> HTTP 404
    - https://silverstaterelief.com/specials -> HTTP 404
    - https://silverstaterelief.com/deals -> HTTP 404

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

## thesource — 1 product-shaped nodes present -- parser should have caught these
- page: https://www.thesourcenv.com/shop
- json payloads: 11 (hosts: {'lab.alpineiq.com': 7, 'freeada.skynettechnologies.com': 1})
- product-shaped nodes: 1
- named, unpriced: 'Libras' keys=['feature_type', 'id', 'name', 'order', 'slug', 'status']
- named, unpriced: 'Voice Navigation' keys=['feature_type', 'id', 'name', 'order', 'slug', 'status']
- named, unpriced: 'Color Blindness' keys=['feature_type', 'id', 'name', 'order', 'slug', 'status']
- named, unpriced: 'Talk & Type' keys=['feature_type', 'id', 'name', 'order', 'slug', 'status']
- urls tried: 4
    - https://www.thesourcenv.com/menu -> JSON captured holds no menu data (wrong URL, or menu loads e
    - https://www.thesourcenv.com/menu/api/menu-top-row?searchFilter=&storeId=4606&exc -> JSON captured holds no menu data (wrong URL, or menu loads e
    - https://www.thesourcenv.com/menu/api/menu-top-row?searchFilter=&storeId=4606&exc -> JSON captured holds no menu data (wrong URL, or menu loads e
    - https://www.thesourcenv.com/shop -> HTTP 404
- paths: data_feature.main_menu[].id, data_feature.main_menu[].name, data_feature.main_menu[].slug, data_feature.main_menu[].order, data_feature.main_menu[].status, data_feature.main_menu[].feature_type, data.ecomLocations[].subEcomLocations[].menuType, data.ecomLocations[].subEcomLocations[].ecomMenuProvider, data.ecomLocations[].ecomMenuProviders, Data.user_package_detail[].price, Data.user_package_detail[].monthly_price, Data.user_package_detail[].price_2

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

## wm_deals — named things present but no price the parser recognizes -- PARSER GAP
- page: https://weedmaps.com/dispensaries/euphoria-wellness
- json payloads: 62 (hosts: {'browser-intake-datadoghq.com': 5, 'api-g.weedmaps.com': 3})
- named, unpriced: '$59 1/2oz Out the Door | Bad Batch Dispos 2/' keys=['body', 'brand_ids', 'categories', 'claimed_count', 'deal_date_id', 'deal_type', 'discount', 'expires_in', 'first_time_customer', 'id', 'likes_count', 'listing', 'menu_item_category_id', 'menu_item_category_names']
- named, unpriced: 'Euphoria Wellness - Marijuana Dispensary' keys=['avatar_image', 'avg_mins_to_complete', 'best_of_weedmaps', 'best_of_weedmaps_nominee', 'best_of_weedmaps_nominee_years', 'best_of_weedmaps_years', 'city', 'deals_enabled', 'distance', 'id', 'is_brand_preferred_listing', 'is_published', 'latitude', 'license_type']
- named, unpriced: 'Las Vegas West / North' keys=['id', 'name', 'slug']
- named, unpriced: 'ROVE' keys=['avatar_image_url', 'id', 'name', 'slug', 'total_deals_count']
- urls tried: 2
    - https://weedmaps.com/deals/united-states/nevada/las-vegas -> named things present but no price the parser recognizes -- P
    - https://weedmaps.com/dispensaries/euphoria-wellness -> named things present but no price the parser recognizes -- P
- paths: data.deals[].menu_item_ids, data.deals[].menu_item_category_names, data.deals[].menu_item_category_id, data.deals[].menu_item_id, data.deals[].price_rule, meta.total_menu_items, meta.has_lab_measured_items, meta.has_live_menu, data.menu_items

## wm_dispos — named things present but no price the parser recognizes -- PARSER GAP
- page: https://weedmaps.com/dispensaries/in/united-states/nevada/las-vegas
- json payloads: 49 (hosts: {'browser-intake-datadoghq.com': 6, 'api-g.weedmaps.com': 1, 'sdk.iad-03.braze.com': 1})
- named, unpriced: 'Vape pens' keys=['avatar_image_url', 'name', 'slug', 'subcategories', 'total_products_count', 'uuid']
- named, unpriced: 'Disposable' keys=['avatar_image_url', 'name', 'slug', 'subcategories', 'total_products_count', 'uuid']
- named, unpriced: 'Cartridge' keys=['avatar_image_url', 'name', 'slug', 'subcategories', 'total_products_count', 'uuid']
- named, unpriced: 'Pods' keys=['avatar_image_url', 'name', 'slug', 'subcategories', 'total_products_count', 'uuid']
- paths: data.facets.categories[].subcategories[].total_products_count, data.facets.client_categories[].subcategories[].total_products_count, data.facets.tag_groups[].tags[].total_products_count, data.facets.categories[].total_products_count, data.facets.price_weights.gram[].units, data.facets.price_weights.gram[].total_products_count, data.facets.price_weights.gram[].label, data.facets.price_weights.gram[].product_count_storefront, data.facets.price_weights.gram[].product_count_delivery, data.facets.client_categories[].total_products_count, data.facets.price_weights.ounce[].units, data.facets.price_weights.ounce[].total_products_count

## zenleaf — 1190 product-shaped nodes present -- parser should have caught these
- page: https://zenleafdispensaries.com/menu
- json payloads: 13 (hosts: {'zenleafdispensaries.com': 4, 'data.zenleafdispensaries.com': 4})
- product-shaped nodes: 1190
- named, unpriced: 'Abington' keys=['address_1', 'address_2', 'bodegaStore', 'city', 'hours', 'lat', 'lng', 'locationId', 'location_status', 'medicalStoreId', 'phoneNumberOverride', 'post_id', 'post_title', 'recreationalStoreId']
- named, unpriced: 'Altoona' keys=['address_1', 'address_2', 'bodegaStore', 'city', 'hours', 'lat', 'lng', 'locationId', 'location_status', 'medicalStoreId', 'phoneNumberOverride', 'post_id', 'post_title', 'recreationalStoreId']
- named, unpriced: 'Antwerp' keys=['address_1', 'address_2', 'bodegaStore', 'city', 'hours', 'lat', 'lng', 'locationId', 'location_status', 'medicalStoreId', 'phoneNumberOverride', 'post_id', 'post_title', 'recreationalStoreId']
- named, unpriced: 'Arcadia' keys=['address_1', 'address_2', 'bodegaStore', 'city', 'hours', 'lat', 'lng', 'locationId', 'location_status', 'medicalStoreId', 'phoneNumberOverride', 'post_id', 'post_title', 'recreationalStoreId']
- paths: products[].id, products[].name, products[].category, products[].category.id, products[].category.name, products[].category.canonicalName, products[].subcategory, products[].subcategory.id, products[].subcategory.name, products[].subcategory.canonicalName, products[].images, products[].brand
