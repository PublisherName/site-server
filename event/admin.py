# Register your models here.
from . import models
from core.base_admin import SummernoteModelAdmin, SummernoteInlineMixin
from django.contrib import admin
from django import forms
from nested_admin import (
    NestedStackedInline,
    NestedModelAdmin,
)
from django.utils.html import format_html


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ["event", "start_time", "end_time"]
    search_fields = ["event", "start_time", "end_time"]


class EventScheduleInline(SummernoteInlineMixin, NestedStackedInline):
    model = models.Schedule
    extra = 1
    autocomplete_fields = ["speakers"]


class EventImagesInline(SummernoteInlineMixin, NestedStackedInline):
    model = models.EventImage
    extra = 1


class EventAdminForms(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = "__all__"
        help_texts = {
            "slug": "This is a unique identifier for the event",
            "title": "This is the title of the event",
            "start_date": "This is the date the event will start",
            "end_date": "This is the date the event will end",
            "description": "This is the description of the event",
            "rsvp_url": "This is the link to the RSVP page",
            "add_to_calender_url": "Add the event to your calendar",
            "is_draft": "This is the status of the event",
            "max_capacity": "This is the maximum capacity of the event",
            "price": "This is the price of the event",
            "registration_deadline": "This is the deadline for registration",
            "event_type": "What type of event is this",
            "location": "This is the location of the event",
            "hot_topics": "Keywords describing the event",
        }


@admin.register(models.Event)
class EventModelAdmin(NestedModelAdmin, SummernoteModelAdmin):
    form = EventAdminForms
    list_display = ["title", "is_draft", "start_date", "price", "get_rsvp_url"]
    search_fields = ["slug", "title"]
    readonly_fields = ["created_at", "updated_at", "slug"]
    inlines = [
        EventScheduleInline,
        EventImagesInline,
    ]
    autocomplete_fields = ["location", "event_type", "hot_topics"]

    def get_rsvp_url(self, obj):
        return format_html(
            '<a href="{}" target="_blank">' + obj.title + "</a>",
            obj.rsvp_url,
        )

    get_rsvp_url.short_description = "RSVP URL"

    def get_rsvp_url(self, obj):
        return format_html(
            '<a href="{}" target="_blank">' + obj.title + "</a>",
            obj.rsvp_url,
        )

    get_rsvp_url.short_description = "RSVP URL"

    def get_rsvp_url(self, obj):
        return format_html(
            '<a href="{}" target="_blank">' + obj.title + "</a>",
            obj.rsvp_url,
        )

    get_rsvp_url.short_description = "RSVP URL"


@admin.register(models.Speaker)
class SpeakersAdmin(SummernoteInlineMixin, admin.ModelAdmin):
    list_display = ["name", "profession", "linkedin", "twitter"]
    search_fields = ["name", "profession"]


@admin.register(models.EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(models.EventLocation)
class EventLocationAdmin(admin.ModelAdmin):
    list_display = ["name", "get_google_map_location"]
    search_fields = ["name"]

    def get_google_map_location(self, obj):
        return format_html(
            '<a href="{}" target="_blank">View on Google Maps</a>',
            obj.google_maps_location,
        )

    get_google_map_location.short_description = "Google Maps Location"


@admin.register(models.HotTopic)
class HotTopicAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


admin.site.register(
    [
        models.EventImage,
    ],
    SummernoteModelAdmin,
)
