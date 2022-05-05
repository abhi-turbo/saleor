import pytest

from .....graphql.tests.queries import subscription_queries
from .....webhook.event_types import WebhookEventAsyncType
from .....webhook.models import Webhook


@pytest.fixture
def subscription_webhook(webhook_app):
    def fun(query, event_type, name="Subscription"):
        webhook = Webhook.objects.create(
            name=name,
            app=webhook_app,
            target_url="http://www.example.com/any",
            subscription_query=query,
        )
        webhook.events.create(event_type=event_type)
        return webhook

    return fun


@pytest.fixture
def subscription_category_created_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.CATEGORY_CREATED,
        WebhookEventAsyncType.CATEGORY_CREATED
    )


@pytest.fixture
def subscription_category_updated_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.CATEGORY_UPDATED,
        WebhookEventAsyncType.CATEGORY_UPDATED
    )


@pytest.fixture
def subscription_category_deleted_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.CATEGORY_DELETED,
        WebhookEventAsyncType.CATEGORY_DELETED
    )


CHANNEL_CREATED_SUBSCRIPTION_QUERY = """
    subscription{
      event{
        ...on ChannelCreated{
          channel{
            id
          }
        }
      }
    }
"""


@pytest.fixture
def subscription_channel_created_webhook(subscription_webhook):
    return subscription_webhook(
        CHANNEL_CREATED_SUBSCRIPTION_QUERY, WebhookEventAsyncType.CHANNEL_CREATED
    )


CHANNEL_UPDATED_SUBSCRIPTION_QUERY = """
    subscription{
      event{
        ...on ChannelUpdated{
          channel{
            id
          }
        }
      }
    }
"""


@pytest.fixture
def subscription_channel_updated_webhook(subscription_webhook):
    return subscription_webhook(
        CHANNEL_UPDATED_SUBSCRIPTION_QUERY, WebhookEventAsyncType.CHANNEL_UPDATED
    )


CHANNEL_DELETED_SUBSCRIPTION_QUERY = """
    subscription{
      event{
        ...on ChannelDeleted{
          channel{
            id
          }
        }
      }
    }
"""


@pytest.fixture
def subscription_channel_deleted_webhook(subscription_webhook):
    return subscription_webhook(
        CHANNEL_DELETED_SUBSCRIPTION_QUERY, WebhookEventAsyncType.CHANNEL_DELETED
    )


CHANNEL_STATUS_CHANGED_SUBSCRIPTION_QUERY = """
    subscription{
      event{
        ...on ChannelStatusChanged{
          channel{
            id
            isActive
          }
        }
      }
    }
"""


@pytest.fixture
def subscription_channel_status_changed_webhook(subscription_webhook):
    return subscription_webhook(
        CHANNEL_STATUS_CHANGED_SUBSCRIPTION_QUERY,
        WebhookEventAsyncType.CHANNEL_STATUS_CHANGED,
    )


GIFT_CARD_DETAILS_FRAGMENT = """
    fragment GiftCardDetails on GiftCard{
        id
        isActive
        code
        createdBy {
            email
        }
    }
"""

GIFT_CARD_CREATED_SUBSCRIPTION_QUERY = (
    GIFT_CARD_DETAILS_FRAGMENT
    + """
    subscription{
      event{
        ...on GiftCardCreated{
          giftCard{
            ...GiftCardDetails
          }
        }
      }
    }
"""
)


@pytest.fixture
def subscription_gift_card_created_webhook(subscription_webhook):
    return subscription_webhook(
        GIFT_CARD_CREATED_SUBSCRIPTION_QUERY, WebhookEventAsyncType.GIFT_CARD_CREATED
    )


GIFT_CARD_UPDATED_SUBSCRIPTION_QUERY = (
    GIFT_CARD_DETAILS_FRAGMENT
    + """
    subscription{
      event{
        ...on GiftCardUpdated{
          giftCard{
            ...GiftCardDetails
          }
        }
      }
    }
"""
)


@pytest.fixture
def subscription_gift_card_updated_webhook(subscription_webhook):
    return subscription_webhook(
        GIFT_CARD_UPDATED_SUBSCRIPTION_QUERY, WebhookEventAsyncType.GIFT_CARD_UPDATED
    )


GIFT_CARD_DELETED_SUBSCRIPTION_QUERY = (
    GIFT_CARD_DETAILS_FRAGMENT
    + """
    subscription{
      event{
        ...on GiftCardDeleted{
          giftCard{
            ...GiftCardDetails
          }
        }
      }
    }
"""
)


@pytest.fixture
def subscription_gift_card_deleted_webhook(subscription_webhook):
    return subscription_webhook(
        GIFT_CARD_DELETED_SUBSCRIPTION_QUERY, WebhookEventAsyncType.GIFT_CARD_DELETED
    )


GIFT_CARD_STATUS_CHANGED_SUBSCRIPTION_QUERY = (
    GIFT_CARD_DETAILS_FRAGMENT
    + """
    subscription{
      event{
        ...on GiftCardStatusChanged{
          giftCard{
            ...GiftCardDetails
          }
        }
      }
    }
"""
)


@pytest.fixture
def subscription_gift_card_status_changed_webhook(subscription_webhook):
    return subscription_webhook(
        GIFT_CARD_STATUS_CHANGED_SUBSCRIPTION_QUERY,
        WebhookEventAsyncType.GIFT_CARD_STATUS_CHANGED,
    )


MENU_DETAILS_FRAGMENT = """
    fragment MenuDetails on Menu{
        id
        name
        slug
        items {
            id
            name
        }
    }
"""

MENU_CREATED_SUBSCRIPTION_QUERY = (
    MENU_DETAILS_FRAGMENT
    + """
    subscription{
      event{
        ...on MenuCreated{
          menu{
            ...MenuDetails
          }
        }
      }
    }
"""
)


@pytest.fixture
def subscription_menu_created_webhook(subscription_webhook):
    return subscription_webhook(
        MENU_CREATED_SUBSCRIPTION_QUERY, WebhookEventAsyncType.MENU_CREATED
    )


MENU_UPDATED_SUBSCRIPTION_QUERY = (
    MENU_DETAILS_FRAGMENT
    + """
    subscription{
      event{
        ...on MenuUpdated{
          menu{
            ...MenuDetails
          }
        }
      }
    }
"""
)


@pytest.fixture
def subscription_menu_updated_webhook(subscription_webhook):
    return subscription_webhook(
        MENU_UPDATED_SUBSCRIPTION_QUERY, WebhookEventAsyncType.MENU_UPDATED
    )


MENU_DELETED_SUBSCRIPTION_QUERY = (
    MENU_DETAILS_FRAGMENT
    + """
    subscription{
      event{
        ...on MenuDeleted{
          menu{
            ...MenuDetails
          }
        }
      }
    }
"""
)


@pytest.fixture
def subscription_menu_deleted_webhook(subscription_webhook):
    return subscription_webhook(
        MENU_DELETED_SUBSCRIPTION_QUERY, WebhookEventAsyncType.MENU_DELETED
    )


MENU_ITEM_DETAILS_FRAGMENT = """
    fragment MenuItemDetails on MenuItem{
        id
        name
        menu {
            id
        }
        page {
            id
        }
    }
"""

MENU_ITEM_CREATED_SUBSCRIPTION_QUERY = (
    MENU_ITEM_DETAILS_FRAGMENT
    + """
    subscription{
      event{
        ...on MenuItemCreated{
          menuItem{
            ...MenuItemDetails
          }
        }
      }
    }
"""
)


@pytest.fixture
def subscription_menu_item_created_webhook(subscription_webhook):
    return subscription_webhook(
        MENU_ITEM_CREATED_SUBSCRIPTION_QUERY, WebhookEventAsyncType.MENU_ITEM_CREATED
    )


MENU_ITEM_UPDATED_SUBSCRIPTION_QUERY = (
    MENU_ITEM_DETAILS_FRAGMENT
    + """
    subscription{
      event{
        ...on MenuItemUpdated{
          menuItem{
            ...MenuItemDetails
          }
        }
      }
    }
"""
)


@pytest.fixture
def subscription_menu_item_updated_webhook(subscription_webhook):
    return subscription_webhook(
        MENU_ITEM_UPDATED_SUBSCRIPTION_QUERY, WebhookEventAsyncType.MENU_ITEM_UPDATED
    )


MENU_ITEM_DELETED_SUBSCRIPTION_QUERY = (
    MENU_ITEM_DETAILS_FRAGMENT
    + """
    subscription{
      event{
        ...on MenuItemDeleted{
          menuItem{
            ...MenuItemDetails
          }
        }
      }
    }
"""
)


@pytest.fixture
def subscription_menu_item_deleted_webhook(subscription_webhook):
    return subscription_webhook(
        MENU_ITEM_DELETED_SUBSCRIPTION_QUERY, WebhookEventAsyncType.MENU_ITEM_DELETED
    )


SHIPPING_PRICE_CREATED_SUBSCRIPTION_QUERY = """
    subscription{
      event{
        ...on ShippingPriceCreated{
          shippingMethod{
            id
            name
            channelListings {
              channel {
                name
              }
            }
          }
          shippingZone{
            id
            name
          }
        }
      }
    }
"""


@pytest.fixture
def subscription_shipping_price_created_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.SHIPPING_PRICE_CREATED,
        WebhookEventAsyncType.SHIPPING_PRICE_CREATED,
    )


@pytest.fixture
def subscription_shipping_price_updated_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.SHIPPING_PRICE_UPDATED_UPDATED,
        WebhookEventAsyncType.SHIPPING_PRICE_UPDATED,
    )


@pytest.fixture
def subscription_shipping_price_deleted_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.SHIPPING_PRICE_DELETED,
        WebhookEventAsyncType.SHIPPING_PRICE_DELETED,
    )


@pytest.fixture
def subscription_shipping_zone_created_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.SHIPPING_ZONE_CREATED,
        WebhookEventAsyncType.SHIPPING_ZONE_CREATED,
    )


@pytest.fixture
def subscription_shipping_zone_updated_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.SHIPPING_ZONE_UPDATED_UPDATED,
        WebhookEventAsyncType.SHIPPING_ZONE_UPDATED,
    )


@pytest.fixture
def subscription_shipping_zone_deleted_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.SHIPPING_ZONE_DELETED,
        WebhookEventAsyncType.SHIPPING_ZONE_DELETED,
    )


@pytest.fixture
def subscription_product_updated_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.PRODUCT_UPDATED,
        WebhookEventAsyncType.PRODUCT_UPDATED
    )


@pytest.fixture
def subscription_product_created_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.PRODUCT_CREATED,
        WebhookEventAsyncType.PRODUCT_CREATED
    )


@pytest.fixture
def subscription_product_deleted_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.PRODUCT_DELETED,
        WebhookEventAsyncType.PRODUCT_DELETED
    )


@pytest.fixture
def subscription_product_variant_created_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.PRODUCT_VARIANT_CREATED,
        WebhookEventAsyncType.PRODUCT_VARIANT_CREATED,
    )


@pytest.fixture
def subscription_product_variant_updated_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.PRODUCT_VARIANT_UPDATED,
        WebhookEventAsyncType.PRODUCT_VARIANT_UPDATED,
    )


@pytest.fixture
def subscription_product_variant_deleted_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.PRODUCT_VARIANT_DELETED,
        WebhookEventAsyncType.PRODUCT_VARIANT_DELETED,
    )


@pytest.fixture
def subscription_product_variant_out_of_stock_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.PRODUCT_VARIANT_OUT_OF_STOCK,
        WebhookEventAsyncType.PRODUCT_VARIANT_OUT_OF_STOCK,
    )


@pytest.fixture
def subscription_product_variant_back_in_stock_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.PRODUCT_VARIANT_BACK_IN_STOCK,
        WebhookEventAsyncType.PRODUCT_VARIANT_BACK_IN_STOCK,
    )


@pytest.fixture
def subscription_order_created_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.ORDER_CREATED,
        WebhookEventAsyncType.ORDER_CREATED
    )


@pytest.fixture
def subscription_order_updated_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.ORDER_UPDATED,
        WebhookEventAsyncType.ORDER_UPDATED
    )


@pytest.fixture
def subscription_order_confirmed_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.ORDER_CONFIRMED,
        WebhookEventAsyncType.ORDER_CONFIRMED
    )


@pytest.fixture
def subscription_order_fully_paid_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.ORDER_FULLY_PAID,
        WebhookEventAsyncType.ORDER_FULLY_PAID
    )

@pytest.fixture
def subscription_order_cancelled_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.ORDER_CANCELLED,
        WebhookEventAsyncType.ORDER_CANCELLED
    )


@pytest.fixture
def subscription_order_fulfilled_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.ORDER_FULFILLED,
        WebhookEventAsyncType.ORDER_FULFILLED
    )


@pytest.fixture
def subscription_draft_order_created_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.DRAFT_ORDER_CREATED,
        WebhookEventAsyncType.DRAFT_ORDER_CREATED,
    )


@pytest.fixture
def subscription_draft_order_updated_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.DRAFT_ORDER_UPDATED,
        WebhookEventAsyncType.DRAFT_ORDER_UPDATED,
    )

@pytest.fixture
def subscription_draft_order_deleted_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.DRAFT_ORDER_DELETED,
        WebhookEventAsyncType.DRAFT_ORDER_DELETED,
    )


@pytest.fixture
def subscription_sale_created_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.SALE_CREATED,
        WebhookEventAsyncType.SALE_CREATED
    )


@pytest.fixture
def subscription_sale_updated_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.SALE_UPDATED,
        WebhookEventAsyncType.SALE_UPDATED
    )

@pytest.fixture
def subscription_sale_deleted_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.SALE_DELETED,
        WebhookEventAsyncType.SALE_DELETED
    )



@pytest.fixture
def subscription_invoice_requested_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.INVOICE_REQUESTED,
        WebhookEventAsyncType.INVOICE_REQUESTED
    )


@pytest.fixture
def subscription_invoice_deleted_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.INVOICE_DELETED,
        WebhookEventAsyncType.INVOICE_DELETED
    )


@pytest.fixture
def subscription_invoice_sent_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.INVOICE_SENT,
        WebhookEventAsyncType.INVOICE_SENT
    )


@pytest.fixture
def subscription_fulfillment_created_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.FULFILLMENT_CREATED,
        WebhookEventAsyncType.FULFILLMENT_CREATED,
    )



@pytest.fixture
def subscription_fulfillment_canceled_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.FULFILLMENT_CANCELED,
        WebhookEventAsyncType.FULFILLMENT_CANCELED,
    )



@pytest.fixture
def subscription_customer_created_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.CUSTOMER_CREATED,
        WebhookEventAsyncType.CUSTOMER_CREATED
    )


@pytest.fixture
def subscription_customer_updated_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.CUSTOMER_UPDATED,
        WebhookEventAsyncType.CUSTOMER_UPDATED
    )

@pytest.fixture
def subscription_collection_created_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.COLLECTION_CREATED,
        WebhookEventAsyncType.COLLECTION_CREATED
    )


@pytest.fixture
def subscription_collection_updated_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.COLLECTION_UPDATED,
        WebhookEventAsyncType.COLLECTION_UPDATED
    )



@pytest.fixture
def subscription_collection_deleted_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.COLLECTION_DELETED,
        WebhookEventAsyncType.COLLECTION_DELETED
    )


@pytest.fixture
def subscription_checkout_created_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.CHECKOUT_CREATED,
        WebhookEventAsyncType.CHECKOUT_CREATED
    )


@pytest.fixture
def subscription_checkout_updated_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.CHECKOUT_UPDATED,
        WebhookEventAsyncType.CHECKOUT_UPDATED
    )


@pytest.fixture
def subscription_page_created_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.PAGE_CREATED,
        WebhookEventAsyncType.PAGE_CREATED
    )


@pytest.fixture
def subscription_page_updated_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.PAGE_UPDATED,
        WebhookEventAsyncType.PAGE_UPDATED,
    )


@pytest.fixture
def subscription_page_deleted_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.PAGE_DELETED,
        WebhookEventAsyncType.PAGE_DELETED,
    )


@pytest.fixture
def subscription_product_created_multiple_events_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.MULTIPLE_EVENTS,
        WebhookEventAsyncType.TRANSLATION_CREATED,
    )


@pytest.fixture
def subscription_translation_created_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.TRANSLATION_CREATED,
        WebhookEventAsyncType.TRANSLATION_CREATED,
    )


@pytest.fixture
def subscription_translation_updated_webhook(subscription_webhook):
    return subscription_webhook(
        subscription_queries.TRANSLATION_UPDATED,
        WebhookEventAsyncType.TRANSLATION_UPDATED,
    )


VOUCHER_DETAILS_FRAGMENT = """
    fragment VoucherDetails on Voucher{
        id
        name
        code
        usageLimit
    }
"""

VOUCHER_CREATED_SUBSCRIPTION_QUERY = (
    VOUCHER_DETAILS_FRAGMENT
    + """
    subscription{
      event{
        ...on VoucherCreated{
          voucher{
            ...VoucherDetails
          }
        }
      }
    }
"""
)


@pytest.fixture
def subscription_voucher_created_webhook(subscription_webhook):
    return subscription_webhook(
        VOUCHER_CREATED_SUBSCRIPTION_QUERY, WebhookEventAsyncType.VOUCHER_CREATED
    )


VOUCHER_UPDATED_SUBSCRIPTION_QUERY = (
    VOUCHER_DETAILS_FRAGMENT
    + """
    subscription{
      event{
        ...on VoucherUpdated{
          voucher{
            ...VoucherDetails
          }
        }
      }
    }
"""
)


@pytest.fixture
def subscription_voucher_updated_webhook(subscription_webhook):
    return subscription_webhook(
        VOUCHER_UPDATED_SUBSCRIPTION_QUERY, WebhookEventAsyncType.VOUCHER_UPDATED
    )


VOUCHER_DELETED_SUBSCRIPTION_QUERY = (
    VOUCHER_DETAILS_FRAGMENT
    + """
    subscription{
      event{
        ...on VoucherDeleted{
          voucher{
            ...VoucherDetails
          }
        }
      }
    }
"""
)


@pytest.fixture
def subscription_voucher_deleted_webhook(subscription_webhook):
    return subscription_webhook(
        VOUCHER_DELETED_SUBSCRIPTION_QUERY, WebhookEventAsyncType.VOUCHER_DELETED
    )
