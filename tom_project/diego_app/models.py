# models.py
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.urls import reverse


class Home(models.Model):
    """Model for the Home section content."""
    name = models.CharField(
        max_length=100,
        default="Diego Tomas Dominguez",
        help_text="Your full name displayed on the homepage."
    )
    quote = models.CharField(
        max_length=255,
        default="The best way to predict the future is to build it.",
        help_text="Your personal quote or tagline."
    )
    profile_image = models.ImageField(
        upload_to='profile/',
        blank=True,
        null=True,
        help_text="Upload your profile photo (recommended size: 400x400px)."
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Only one home section can be active at a time."
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Home Section"
        verbose_name_plural = "Home Section"
        # Ensure only one active home section exists
        constraints = [
            models.UniqueConstraint(
                fields=['is_active'],
                condition=models.Q(is_active=True),
                name='unique_active_home'
            )
        ]

    def __str__(self):
        return f"Home - {self.name}"

    def save(self, *args, **kwargs):
        """If this instance is being set as active, deactivate all others."""
        if self.is_active:
            Home.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

# ----------------------------------------------------------------------
# Base / Abstract Models
# ----------------------------------------------------------------------
class BaseModel(models.Model):
    """Abstract base model with common fields for ordering and timestamps."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.PositiveIntegerField(default=0, help_text="Order in which this item appears.")

    class Meta:
        abstract = True
        ordering = ['order', '-created_at']


# ----------------------------------------------------------------------
# About Section
# ----------------------------------------------------------------------
class About(models.Model):
    """Single model for the About Me section content."""
    content = models.TextField(
        help_text="The full 'About Me' text. You can use HTML formatting if needed."
    )
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "About"

    def __str__(self):
        return "About Me (Active)" if self.is_active else "About Me (Inactive)"


# ----------------------------------------------------------------------
# Skill Models
# ----------------------------------------------------------------------
class Skill(models.Model):
    """Represents a programming language or technology skill."""
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(
        help_text="Brief description of the skill and its usage."
    )
    proficiency = models.PositiveSmallIntegerField(
        help_text="Skill level percentage (0-100).",
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]  # Fixed this line
    )
    order = models.PositiveIntegerField(default=0, help_text="Display order.")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} - {self.proficiency}%"


# ----------------------------------------------------------------------
# Project Models
# ----------------------------------------------------------------------
class Project(models.Model):
    """Represents a project in the portfolio."""
    name = models.CharField(max_length=200)
    description = models.TextField(help_text="Detailed description of the project.")
    # Optional fields for richer content
    url = models.URLField(blank=True, help_text="Live project URL, if available.")
    github_url = models.URLField(blank=True, help_text="GitHub repository link.")
    image = models.ImageField(
        upload_to='projects/',
        blank=True,
        null=True,
        help_text="Optional project screenshot or logo."
    )
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.name

    def get_tags_list(self):
        """Return list of tags associated with this project.""" 
        # Use the through model to get ordered tags
        tag_links = self.tag_links.select_related('tag').all()
        return [link.tag.name for link in tag_links]


class ProjectTag(models.Model):
    """Tag for categorizing projects (e.g., Python, Django, HTML)."""
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProjectTagLink(models.Model):
    """Many-to-many through model for ordering tags on a project."""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tag_links')
    tag = models.ForeignKey(ProjectTag, on_delete=models.CASCADE, related_name='project_links')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        unique_together = ['project', 'tag']


# ----------------------------------------------------------------------
# Education Models
# ----------------------------------------------------------------------
class Education(models.Model):
    """Represents an educational milestone."""
    STATUS_CHOICES = [
        ('graduated', 'Graduated'),
        ('ongoing', 'Currently Studying'),
        ('dropped', 'Dropped'),
        ('other', 'Other'),
    ]

    level = models.CharField(max_length=100, help_text="e.g., Elementary, High School, College")
    institution = models.CharField(max_length=200, help_text="Name of the school/university.")
    description = models.TextField(blank=True, help_text="Additional details, honors, etc.")
    start_year = models.PositiveSmallIntegerField(null=True, blank=True)
    end_year = models.PositiveSmallIntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ongoing')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    # For "ongoing" status, optionally show expected graduation
    expected_graduation = models.CharField(max_length=50, blank=True, help_text="e.g., 2025")

    class Meta:
        verbose_name_plural = "Education"
        ordering = ['order', '-end_year', '-start_year']

    def __str__(self):
        return f"{self.level} - {self.institution}"


# ----------------------------------------------------------------------
# Contact & Message Models
# ----------------------------------------------------------------------
class ContactInfo(models.Model):
    """Contact details like email, LinkedIn, GitHub, Twitter."""
    CONTACT_TYPES = [
        ('email', 'Email'),
        ('linkedin', 'LinkedIn'),
        ('github', 'GitHub'),
        ('twitter', 'Twitter / X'),
        ('other', 'Other'),
    ]

    contact_type = models.CharField(max_length=20, choices=CONTACT_TYPES, unique=True)
    label = models.CharField(max_length=50, blank=True, help_text="Display label, e.g., 'Email'")
    value = models.CharField(max_length=255, help_text="The actual email/URL/username")
    url = models.URLField(blank=True, help_text="Full URL for clickable links")
    icon = models.CharField(max_length=10, blank=True, help_text="Emoji or icon char")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.get_contact_type_display()}: {self.value}"


class ContactMessage(models.Model):
    """Store messages submitted via the contact form."""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False, help_text="Mark as read in admin.")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"


# ----------------------------------------------------------------------
# Site Configuration (optional)
# ----------------------------------------------------------------------
class SiteConfig(models.Model):
    """Key-value store for site-wide configuration."""
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField(blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Site configurations"

    def __str__(self):
        return self.key