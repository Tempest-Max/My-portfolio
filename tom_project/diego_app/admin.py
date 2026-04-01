from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from . import models


@admin.register(models.Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['name', 'quote_preview', 'has_profile_image', 'is_active', 'updated_at']
    list_editable = ['is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'quote']
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'quote', 'profile_image')
        }),
        ('Status', {
            'fields': ('is_active',),
            'description': 'Only one home section can be active at a time. Setting this to active will automatically deactivate others.'
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at', 'updated_at']

    def quote_preview(self, obj):
        """Display a preview of the quote in the list."""
        return obj.quote[:50] + '…' if len(obj.quote) > 50 else obj.quote
    quote_preview.short_description = 'Quote Preview'

    def has_profile_image(self, obj):
        """Show if a profile image exists."""
        return bool(obj.profile_image)
    has_profile_image.boolean = True
    has_profile_image.short_description = 'Has Photo'

    def get_actions(self, request):
        """Customize admin actions."""
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        """Prevent deletion of home section to maintain at least one record."""
        if obj and models.Home.objects.count() <= 1:
            return False
        return super().has_delete_permission(request, obj)

# ----------------------------------------------------------------------
# Inline Admins
# ----------------------------------------------------------------------
class ProjectTagLinkInline(admin.TabularInline):
    model = models.ProjectTagLink
    extra = 1
    autocomplete_fields = ['tag']
    fields = ['tag', 'order']
    ordering = ['order']


# ----------------------------------------------------------------------
# Model Admins
# ----------------------------------------------------------------------
@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'content_preview', 'is_active', 'updated_at']
    list_editable = ['is_active']
    fields = ['content', 'is_active']

    def content_preview(self, obj):
        return obj.content[:100] + '…' if len(obj.content) > 100 else obj.content
    content_preview.short_description = 'Content Preview'


@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'proficiency', 'order', 'is_active']
    list_editable = ['proficiency', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'description']
    fields = ['name', 'description', 'proficiency', 'order', 'is_active']


@admin.register(models.ProjectTag)
class ProjectTagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'is_active', 'created_at']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    inlines = [ProjectTagLinkInline]
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'is_active')
        }),
        ('Links & Media', {
            'fields': ('url', 'github_url', 'image'),
            'classes': ('collapse',)
        }),
        ('Display', {
            'fields': ('order',)
        }),
    )

    def tag_list(self, obj):
        tags = obj.tags.all()
        return ", ".join(tag.name for tag in tags)
    tag_list.short_description = 'Tags'


@admin.register(models.Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['level', 'institution', 'status', 'order', 'is_active']
    list_editable = ['order', 'is_active', 'status']
    list_filter = ['status', 'is_active']
    search_fields = ['level', 'institution', 'description']
    fieldsets = (
        (None, {
            'fields': ('level', 'institution', 'description', 'status')
        }),
        ('Dates', {
            'fields': ('start_year', 'end_year', 'expected_graduation'),
            'classes': ('collapse',)
        }),
        ('Display', {
            'fields': ('order', 'is_active')
        }),
    )


@admin.register(models.ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['contact_type', 'value', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['contact_type', 'is_active']
    search_fields = ['value', 'label']


@admin.register(models.ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_editable = ['is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
    actions = ['mark_as_read']

    def has_add_permission(self, request):
        return False  # Messages are only created via frontend form

    def mark_as_read(self, request, queryset):
        updated = queryset.update(is_read=True)
        self.message_user(request, f"{updated} message(s) marked as read.")
    mark_as_read.short_description = "Mark selected messages as read"


@admin.register(models.SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    list_display = ['key', 'value_preview', 'description']
    search_fields = ['key', 'description']
    fields = ['key', 'value', 'description']

    def value_preview(self, obj):
        return obj.value[:50] + '…' if len(obj.value) > 50 else obj.value
    value_preview.short_description = 'Value'


# ----------------------------------------------------------------------
# Optional: Dashboard customization (if you want to see stats)
# ----------------------------------------------------------------------
class CustomAdminSite(admin.AdminSite):
    site_header = "Diego Tomas Dominguez Portfolio Admin"
    site_title = "Portfolio Admin"
    index_title = "Dashboard"

    def get_app_list(self, request):
        app_list = super().get_app_list(request)
        # You can add custom dashboard metrics here
        return app_list

