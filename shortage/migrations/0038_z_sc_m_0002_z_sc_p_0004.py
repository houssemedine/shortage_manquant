# Generated by Django 4.0.4 on 2022-06-13 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortage', '0037_alter_zmm_carnet_cde_is_quantity_to_receive'),
    ]

    operations = [
        migrations.CreateModel(
            name='Z_SC_M_0002',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(null=True)),
                ('week', models.IntegerField(null=True)),
                ('uploaded_by', models.IntegerField(null=True)),
                ('uploaded_at', models.DateTimeField(null=True)),
                ('material', models.CharField(max_length=30, null=True)),
                ('num_material', models.CharField(max_length=100, null=True)),
                ('division', models.IntegerField(null=True)),
                ('orga', models.CharField(max_length=30, null=True)),
                ('tyar', models.CharField(max_length=30, null=True)),
                ('sa', models.CharField(max_length=30, null=True)),
                ('a_s1', models.CharField(max_length=30, null=True)),
                ('fra', models.CharField(max_length=10, null=True)),
                ('vendor', models.CharField(max_length=20, null=True)),
                ('name1', models.CharField(max_length=50, null=True)),
                ('contract', models.CharField(max_length=30, null=True)),
                ('post', models.CharField(max_length=30, null=True)),
                ('purchase_info', models.CharField(max_length=30, null=True)),
                ('uq1', models.CharField(max_length=30, null=True)),
                ('gest1', models.CharField(max_length=30, null=True)),
                ('val_arrondie', models.FloatField(null=True)),
                ('uq2', models.CharField(max_length=30, null=True)),
                ('orig', models.CharField(max_length=30, null=True)),
                ('gac1', models.CharField(max_length=30, null=True)),
                ('tps_de_recep', models.CharField(max_length=30, null=True)),
                ('dpl', models.CharField(max_length=30, null=True)),
                ('uac1', models.CharField(max_length=30, null=True)),
                ('px_busgt_cours', models.FloatField(null=True)),
                ('dev1', models.CharField(max_length=30, null=True)),
                ('pbudg_prec', models.FloatField(null=True)),
                ('dev2', models.CharField(max_length=30, null=True)),
                ('futur_budget_price', models.FloatField(null=True)),
                ('dev3', models.CharField(max_length=30, null=True)),
                ('par1', models.IntegerField(null=True)),
                ('cival', models.CharField(max_length=30, null=True)),
                ('por', models.CharField(max_length=30, null=True)),
                ('sgf', models.CharField(max_length=30, null=True)),
                ('num_material_fourn1', models.CharField(max_length=100, null=True)),
                ('gac2', models.CharField(max_length=30, null=True)),
                ('dpr1', models.IntegerField(null=True)),
                ('net_price', models.FloatField(null=True)),
                ('dev4', models.CharField(max_length=30, null=True)),
                ('par2', models.IntegerField(null=True)),
                ('inctm', models.CharField(max_length=30, null=True)),
                ('incpterms', models.CharField(max_length=50, null=True)),
                ('qte_standard', models.FloatField(null=True)),
                ('uac2', models.CharField(max_length=30, null=True)),
                ('qte_min', models.FloatField(null=True)),
                ('uac3', models.CharField(max_length=30, null=True)),
                ('name2', models.IntegerField(null=True)),
                ('uac4', models.CharField(max_length=30, null=True)),
                ('corr', models.IntegerField(null=True)),
                ('post_type', models.CharField(max_length=30, null=True)),
                ('target_qte', models.FloatField(null=True)),
                ('uac5', models.CharField(max_length=30, null=True)),
                ('gac3', models.CharField(max_length=30, null=True)),
                ('price_net', models.FloatField(null=True)),
                ('dev5', models.CharField(max_length=30, null=True)),
                ('dev6', models.CharField(max_length=30, null=True)),
                ('par3', models.IntegerField(null=True)),
                ('i', models.CharField(max_length=30, null=True)),
                ('num_material_fourn2', models.CharField(max_length=100, null=True)),
                ('tre', models.FloatField(null=True)),
                ('tps_fab_ext', models.FloatField(null=True)),
                ('inctm_contract', models.CharField(max_length=30, null=True)),
                ('inctm_contract2', models.CharField(max_length=30, null=True)),
                ('gac4', models.CharField(max_length=30, null=True)),
                ('dev7', models.CharField(max_length=30, null=True)),
                ('inctm2', models.CharField(max_length=30, null=True)),
                ('incoterms2', models.CharField(max_length=30, null=True)),
                ('grpi1', models.CharField(max_length=30, null=True)),
                ('abc', models.CharField(max_length=30, null=True)),
                ('planning_unit', models.CharField(max_length=30, null=True)),
                ('gest2', models.CharField(max_length=30, null=True)),
                ('a_s2', models.CharField(max_length=30, null=True)),
                ('dpr2', models.IntegerField(null=True)),
                ('grpi2', models.CharField(max_length=30, null=True)),
                ('apsc', models.CharField(max_length=30, null=True)),
                ('num_tarif_dnr', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Z_SC_P_0004',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(null=True)),
                ('week', models.IntegerField(null=True)),
                ('uploaded_by', models.IntegerField(null=True)),
                ('uploaded_at', models.DateTimeField(null=True)),
                ('notice', models.CharField(max_length=30, null=True)),
                ('vendor', models.CharField(max_length=20, null=True)),
                ('supplier_account_number', models.CharField(max_length=50, null=True)),
                ('created_on', models.DateTimeField(null=True)),
                ('created_by', models.CharField(max_length=30, null=True)),
                ('system_status', models.CharField(max_length=20, null=True)),
                ('division', models.IntegerField(null=True)),
                ('gac', models.CharField(max_length=30, null=True)),
                ('purchase_document', models.CharField(max_length=30, null=True)),
                ('poste', models.CharField(max_length=30, null=True)),
                ('material', models.CharField(max_length=30, null=True)),
                ('num_material', models.CharField(max_length=100, null=True)),
                ('reference', models.CharField(max_length=100, null=True)),
                ('date', models.DateTimeField(null=True)),
                ('updated_on', models.DateTimeField(null=True)),
                ('updated_by', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
