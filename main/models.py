from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")
    position = models.CharField(max_length=100, verbose_name="Poste")
    bio = models.TextField(verbose_name="Biographie")
    photo = models.ImageField(upload_to='team/', blank=True, null=True, verbose_name="Photo")
    order = models.IntegerField(default=0, verbose_name="Ordre d'affichage")
    
    class Meta:
        ordering = ['order']
        verbose_name = "Membre de l'équipe"
        verbose_name_plural = "Membres de l'équipe"
    
    def __str__(self):
        return self.name

class Partner(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")
    logo = models.ImageField(upload_to='partners/', verbose_name="Logo")
    website = models.URLField(blank=True, verbose_name="Site web")
    
    class Meta:
        verbose_name = "Partenaire"
        verbose_name_plural = "Partenaires"
    
    def __str__(self):
        return self.name

class Project(models.Model):
    STATUS_CHOICES = [
        ('planned', 'Planifié'),
        ('in_progress', 'En cours'),
        ('completed', 'Terminé')
    ]
    
    title = models.CharField(max_length=200, verbose_name="Titre")
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(upload_to='projects/', verbose_name="Image")
    location = models.CharField(max_length=100, verbose_name="Localisation")
    start_date = models.DateField(verbose_name="Date de début")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name="Statut")
    
    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"
        ordering = ['-start_date']
    
    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")
    role = models.CharField(max_length=100, verbose_name="Rôle")
    content = models.TextField(verbose_name="Témoignage")
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True, verbose_name="Photo")
    
    class Meta:
        verbose_name = "Témoignage"
        verbose_name_plural = "Témoignages"
    
    def __str__(self):
        return f"{self.name} - {self.role}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom complet")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Téléphone")
    company = models.CharField(max_length=100, blank=True, verbose_name="Entreprise")
    subject = models.CharField(max_length=200, verbose_name="Sujet")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date d'envoi")
    is_read = models.BooleanField(default=False, verbose_name="Lu")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Message de contact"
        verbose_name_plural = "Messages de contact"
    
    def __str__(self):
        return f"Message de {self.name} - {self.subject}"