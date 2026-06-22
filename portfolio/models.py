from django.db import models
from django.utils.text import slugify


# ==========================================================
# Base Model
# ==========================================================

class BaseModel(models.Model):
    """
    Abstract base model that provides timestamps.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# ==========================================================
# Portfolio Profile
# ==========================================================

class PortfolioProfile(BaseModel):
    """
    Stores all personal information used in Hero, About
    and Contact sections.
    """

    full_name = models.CharField(max_length=120)

    designation = models.CharField(
        max_length=150,
        help_text="Example: Full Stack Developer"
    )

    hero_title = models.CharField(
        max_length=255,
        help_text="Main heading displayed in Hero section."
    )

    hero_description = models.TextField()

    about = models.TextField()

    profile_image = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True
    )

    resume = models.FileField(
        upload_to="resume/",
        blank=True,
        null=True
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    location = models.CharField(
        max_length=120
    )

    map_url = models.URLField(
        blank=True
    )

    available_for_work = models.BooleanField(
        default=True
    )

    class Meta:
        verbose_name = "Portfolio Profile"
        verbose_name_plural = "Portfolio Profile"

    def __str__(self):
        return self.full_name

# ==========================================================
# Social Links
# ==========================================================

class SocialLink(BaseModel):

    PLATFORM_CHOICES = [
        ("GitHub", "GitHub"),
        ("LinkedIn", "LinkedIn"),
        ("Instagram", "Instagram"),
        ("Facebook", "Facebook"),
        ("WhatsApp", "WhatsApp"),
        ("Upwork", "Upwork"),
        ("Fiverr", "Fiverr"),
        ("YouTube", "YouTube"),
    ]

    profile = models.ForeignKey(
        PortfolioProfile,
        on_delete=models.CASCADE,
        related_name="social_links"
    )

    platform = models.CharField(
        max_length=30,
        choices=PLATFORM_CHOICES
    )

    url = models.URLField()

    display_order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.platform


# ==========================================================
# Skills
# ==========================================================

class Skill(BaseModel):

    CATEGORY_CHOICES = [
        ("Frontend", "Frontend"),
        ("Backend", "Backend"),
        ("Database", "Database"),
        ("DevOps", "DevOps"),
        ("Tools", "Tools"),
    ]

    profile = models.ForeignKey(
        PortfolioProfile,
        on_delete=models.CASCADE,
        related_name="skills"
    )

    name = models.CharField(max_length=100)

    icon = models.FileField(
        upload_to="skills/",
        blank=True,
        null=True
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    display_order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["display_order"]
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.name


# ==========================================================
# Hobbies
# ==========================================================

class Hobby(BaseModel):

    profile = models.ForeignKey(
        PortfolioProfile,
        on_delete=models.CASCADE,
        related_name="hobbies"
    )

    title = models.CharField(max_length=100)

    emoji = models.CharField(
        max_length=10
    )

    left_position = models.CharField(max_length=10)

    top_position = models.CharField(max_length=10)

    display_order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.title
    


# ==========================================================
# Projects
# ==========================================================

class Project(BaseModel):

    company = models.CharField(max_length=120)

    year = models.PositiveIntegerField()

    title = models.CharField(max_length=200)

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    description = models.TextField(blank=True)

    image = models.ImageField(
        upload_to="projects/"
    )

    github_url = models.URLField(blank=True)

    live_url = models.URLField()

    featured = models.BooleanField(default=True)

    display_order = models.PositiveIntegerField(default=1)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# ==========================================================
# Project Features
# ==========================================================

class ProjectFeature(BaseModel):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="features"
    )

    title = models.CharField(max_length=255)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.title
    

# ==========================================================
# Project Images
# ==========================================================


class ProjectImage(BaseModel):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="gallery"
    )

    image = models.ImageField(
        upload_to="projects/gallery/"
    )

    caption = models.CharField(
        max_length=200,
        blank=True,
        help_text="Example: Dashboard, Login Page, Analytics"
    )

    display_order = models.PositiveIntegerField(
        default=1
    )

    class Meta:
        ordering = ["display_order"]
        verbose_name = "Project Image"
        verbose_name_plural = "Project Images"

    def __str__(self):
        return f"{self.project.title} - Image {self.display_order}"



# ==========================================================
# Testimonials
# ==========================================================

class Testimonial(BaseModel):

    client_name = models.CharField(max_length=100)

    position = models.CharField(max_length=150)

    review = models.TextField()

    avatar = models.ImageField(
        upload_to="testimonials/"
    )

    display_order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.client_name


# ==========================================================
# Contact Messages
# ==========================================================

class ContactMessage(BaseModel):

    name = models.CharField(max_length=120)

    email = models.EmailField()

    subject = models.CharField(max_length=255)

    message = models.TextField()

    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
    