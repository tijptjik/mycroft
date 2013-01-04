from django.contrib import admin
from paypal.standard.ipn.models import PayPalIPN
from paypal.standard.ipn.admin import PayPalIPNAdmin
from models import *

for model in [Product, Video, Lecturer, Series, Poet, Poem, Testimonial, Preview, Access]:
    admin.site.register(model)


class LectureAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Lecture, LectureAdmin)

class CustomPayPalIPNAdmin(PayPalIPNAdmin):
    def queryset(self, request):
        """Limit Transactions to those that are actually payments"""
        qs = super(CustomPayPalIPNAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs.filter(payment_type='instant')
        return qs

    fieldsets = (
        (None, {
            "fields": [
                "invoice",
                ("txn_id", "txn_type", "payment_status"),
                ("item_name", "item_number"),
                ("mc_gross", "mc_fee","payment_date"),
                "memo"
            ]
        }),
        ("Buyer", {
            "description": "The information about the Buyer.",
            'classes': ('collapse',),
            "fields": [
                ("first_name", "last_name", "payer_business_name"), ("payer_email",
                "payer_id", "payer_status"), ("contact_phone", "residence_country")
            ]
        }),
        ("Recurring", {
            "description": "Information about recurring Payments.",
            "classes": ("collapse",),
            "fields": [
                "profile_status", 
                ("initial_payment_amount", "amount_per_cycle", "outstanding_balance"), "period_type", "product_name", 
                "product_type", "recurring_payment_id", "receipt_id", 
                "next_payment_date"
            ]
        }),
    )
    list_display = [
        "invoice", "payer_id", "payment_status", "item_name", "mc_gross", "created_at"
    ]
    search_fields = ["txn_id", "recurring_payment_id"]


admin.site.unregister(PayPalIPN)
admin.site.register(PayPalIPN, CustomPayPalIPNAdmin)
