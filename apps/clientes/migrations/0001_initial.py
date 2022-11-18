# Generated by Django 4.1.2 on 2022-11-17 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TipoCliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tipo", models.CharField(max_length=50, verbose_name="Tipo")),
                ("created_at", models.DateField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=150, verbose_name="Nome")),
                ("cpf_cnpj", models.CharField(max_length=30, verbose_name="CPF/CNPJ")),
                ("email", models.EmailField(max_length=254, verbose_name="E-mail")),
                ("telefone", models.CharField(max_length=30, verbose_name="Telefone")),
                ("endereco", models.CharField(max_length=200, verbose_name="Endereço")),
                ("bairro", models.CharField(max_length=50, verbose_name="Bairro")),
                (
                    "referencia",
                    models.CharField(max_length=100, verbose_name="Referencia"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="Cadastrado em"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="Modificado em"
                    ),
                ),
                ("slug", models.SlugField(editable=False, max_length=255, unique=True)),
                (
                    "tipo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="clientes.tipocliente",
                        verbose_name="Tipo de Cliente",
                    ),
                ),
            ],
        ),
    ]
