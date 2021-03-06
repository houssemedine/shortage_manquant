# Generated by Django 4.0.2 on 2022-04-26 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ART_MARA_MARC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(null=True)),
                ('week', models.IntegerField(null=True)),
                ('uploaded_by', models.IntegerField(null=True)),
                ('uploaded_at', models.DateTimeField(null=True)),
                ('material', models.CharField(max_length=30, null=True)),
                ('material_designation', models.CharField(max_length=200, null=True)),
                ('text_material', models.CharField(max_length=200, null=True)),
                ('market_group', models.CharField(max_length=30, null=True)),
                ('division', models.IntegerField(null=True)),
                ('ctrpr', models.CharField(max_length=30, null=True)),
                ('typ_app', models.CharField(max_length=30, null=True)),
                ('a_s', models.CharField(max_length=30, null=True)),
                ('tcy', models.IntegerField(null=True)),
                ('dfi', models.IntegerField(null=True)),
                ('dpr', models.IntegerField(null=True)),
                ('horiz', models.CharField(max_length=30, null=True)),
                ('mp', models.FloatField(null=True)),
                ('r', models.FloatField(null=True)),
                ('tyar', models.CharField(max_length=30, null=True)),
                ('nai', models.FloatField(null=True)),
                ('i_c', models.FloatField(null=True)),
                ('aappr_def', models.FloatField(null=True)),
                ('mgApp', models.FloatField(null=True)),
                ('mag', models.FloatField(null=True)),
                ('tl', models.CharField(max_length=30, null=True)),
                ('fixed_batch', models.FloatField(null=True)),
                ('uq1', models.CharField(max_length=30, null=True)),
                ('security_stock', models.FloatField(null=True)),
                ('uq2', models.CharField(max_length=30, null=True)),
                ('tre', models.FloatField(null=True)),
                ('gest', models.CharField(max_length=30, null=True)),
                ('di', models.CharField(max_length=30, null=True)),
                ('scrap', models.FloatField(null=True)),
                ('gac', models.CharField(max_length=30, null=True)),
                ('profile', models.CharField(max_length=30, null=True)),
                ('prpiat', models.CharField(max_length=30, null=True)),
                ('created_by', models.CharField(max_length=30, null=True)),
                ('language', models.CharField(max_length=30, null=True)),
                ('created_on', models.DateTimeField(null=True)),
                ('gcha', models.CharField(max_length=30, null=True)),
                ('gs', models.CharField(max_length=30, null=True)),
                ('comparison_mode_of_the_requirements', models.CharField(max_length=30, null=True)),
                ('int_adjustment_upstream', models.FloatField(null=True)),
                ('int_adjustment_downstream', models.FloatField(null=True)),
                ('size_l_min', models.FloatField(null=True)),
                ('uq3', models.CharField(max_length=30, null=True)),
                ('rounded_value', models.FloatField(null=True)),
                ('uq4', models.CharField(max_length=30, null=True)),
                ('lot_size_mx', models.FloatField(null=True)),
                ('uq5', models.CharField(max_length=30, null=True)),
                ('maximum_stock', models.FloatField(null=True)),
                ('uq6', models.CharField(max_length=30, null=True)),
                ('edge', models.CharField(max_length=30, null=True)),
                ('typ', models.CharField(max_length=30, null=True)),
                ('time_limit1', models.FloatField(null=True)),
                ('time_limit2', models.FloatField(null=True)),
                ('recipient_ctrl', models.CharField(max_length=30, null=True)),
                ('material_filled', models.CharField(max_length=30, null=True)),
                ('dv', models.CharField(max_length=30, null=True)),
                ('gml', models.CharField(max_length=30, null=True)),
                ('grpi', models.CharField(max_length=30, null=True)),
                ('abc', models.CharField(max_length=30, null=True)),
                ('uq7', models.CharField(max_length=30, null=True)),
                ('wbs_element', models.CharField(max_length=30, null=True)),
                ('grpa', models.CharField(max_length=30, null=True)),
                ('control_code', models.CharField(max_length=30, null=True)),
                ('product_hierarchy', models.CharField(max_length=30, null=True)),
                ('gross_weight', models.FloatField(null=True)),
                ('unp1', models.CharField(max_length=30, null=True)),
                ('net_weight', models.FloatField(null=True)),
                ('unp2', models.CharField(max_length=30, null=True)),
                ('no_ccr', models.CharField(max_length=30, null=True)),
                ('ccr_lot_size', models.FloatField(null=True)),
                ('uq8', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Core',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('deleted_by', models.IntegerField(null=True)),
                ('deleted_on', models.DateTimeField(null=True)),
                ('created_on', models.DateTimeField()),
                ('created_by', models.IntegerField(default=1)),
                ('updated_by', models.IntegerField(default=1)),
                ('updated_on', models.DateTimeField()),
                ('material', models.CharField(max_length=10, null=True)),
                ('division', models.CharField(max_length=30, null=True)),
                ('program', models.CharField(max_length=30, null=True)),
                ('supplier', models.CharField(max_length=30, null=True)),
                ('part_number', models.FloatField(null=True)),
                ('type_of_alert', models.CharField(max_length=30, null=True)),
                ('requested_date', models.DateTimeField()),
                ('needed_quantity', models.FloatField(null=True)),
                ('subject', models.TextField(null=True)),
                ('status', models.CharField(default='To do', max_length=30, null=True)),
                ('closing_date', models.DateTimeField(null=True)),
                ('duration_of_the_event', models.CharField(max_length=30, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MB52',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(null=True)),
                ('week', models.IntegerField(null=True)),
                ('uploaded_by', models.IntegerField(null=True)),
                ('uploaded_at', models.DateTimeField(null=True)),
                ('material', models.CharField(max_length=30, null=True)),
                ('division', models.IntegerField(null=True)),
                ('store', models.IntegerField(null=True)),
                ('store_level_deletion_indicator', models.CharField(max_length=15, null=True)),
                ('unit', models.CharField(max_length=5, null=True)),
                ('for_free_use', models.FloatField(null=True)),
                ('currency', models.CharField(max_length=5, null=True)),
                ('value_free_use', models.FloatField(null=True)),
                ('transit_transfer', models.FloatField(null=True)),
                ('transit_transfer_value', models.FloatField(null=True)),
                ('in_quality_control', models.FloatField(null=True)),
                ('value_quality_control', models.FloatField(null=True)),
                ('non_free_stock', models.FloatField(null=True)),
                ('non_free_value', models.FloatField(null=True)),
                ('blocked', models.FloatField(null=True)),
                ('blocked_stock_value', models.FloatField(null=True)),
                ('returns', models.FloatField(null=True)),
                ('blocked_return_stock_value', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MDMA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(null=True)),
                ('week', models.IntegerField(null=True)),
                ('uploaded_by', models.IntegerField(null=True)),
                ('uploaded_at', models.DateTimeField(null=True)),
                ('material', models.CharField(max_length=30, null=True)),
                ('planning_unit', models.CharField(max_length=30, null=True)),
                ('division', models.IntegerField(null=True)),
                ('planning_profile', models.CharField(max_length=30, null=True)),
                ('planning_type', models.CharField(max_length=30, null=True)),
                ('manager', models.CharField(max_length=30, null=True)),
                ('planning_group', models.CharField(max_length=30, null=True)),
                ('order_point', models.FloatField(null=True)),
                ('planning_rate', models.CharField(max_length=30, null=True)),
                ('fixed_planning_horizon', models.FloatField(null=True)),
                ('lot_size_calculation_key', models.CharField(max_length=30, null=True)),
                ('rounding_profile', models.CharField(max_length=30, null=True)),
                ('rounding_value', models.FloatField(null=True)),
                ('minimum_lot_size', models.FloatField(null=True)),
                ('maximum_lot_size', models.FloatField(null=True)),
                ('maximum_stock', models.FloatField(null=True)),
                ('cycle', models.FloatField(null=True)),
                ('rejects_ss_ens', models.FloatField(null=True)),
                ('special_supply', models.CharField(max_length=30, null=True)),
                ('production_store', models.CharField(max_length=30, null=True)),
                ('store_for_external_supply', models.CharField(max_length=30, null=True)),
                ('planning_calendar', models.CharField(max_length=30, null=True)),
                ('safety_stock', models.FloatField(null=True)),
                ('coverage_profile', models.CharField(max_length=30, null=True)),
                ('safety_stock_actual_stock', models.FloatField(null=True)),
                ('fixed_lot_size', models.FloatField(null=True)),
                ('fixed_lot_costs', models.FloatField(null=True)),
                ('storage_cost_code', models.CharField(max_length=30, null=True)),
                ('service_rate', models.FloatField(null=True)),
                ('forecast_profile', models.CharField(max_length=30, null=True)),
                ('ref_cons_val', models.CharField(max_length=30, null=True)),
                ('un_plan_cons', models.CharField(max_length=30, null=True)),
                ('au', models.CharField(max_length=30, null=True)),
                ('multiplier', models.FloatField(null=True)),
                ('suppr_indicator', models.CharField(max_length=30, null=True)),
                ('prof_per_sec', models.CharField(max_length=30, null=True)),
                ('dependent_needs_planner', models.CharField(max_length=30, null=True)),
                ('reset_auto', models.CharField(max_length=30, null=True)),
                ('management_status', models.CharField(max_length=30, null=True)),
                ('correction_pow', models.CharField(max_length=30, null=True)),
                ('safety_time', models.CharField(max_length=30, null=True)),
                ('for_apo', models.CharField(max_length=30, null=True)),
                ('forecast_delivery_time', models.CharField(max_length=30, null=True)),
                ('take_into_account_the_expected_delivery_time', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SE16N_CEPC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(null=True)),
                ('week', models.IntegerField(null=True)),
                ('uploaded_by', models.IntegerField()),
                ('uploaded_at', models.DateTimeField()),
                ('profit_center', models.CharField(max_length=30, null=True)),
                ('valid_to', models.DateTimeField(null=True)),
                ('controlling_area', models.CharField(max_length=30, null=True)),
                ('valid_from', models.DateTimeField(null=True)),
                ('created_on', models.DateTimeField(null=True)),
                ('created_by', models.CharField(max_length=30, null=True)),
                ('field_name_of_CO_PA_characteristic', models.CharField(max_length=30, null=True)),
                ('department', models.CharField(max_length=30, null=True)),
                ('person_responsible_for_profit_center', models.CharField(max_length=30, null=True)),
                ('user_responsible', models.CharField(max_length=30, null=True)),
                ('currency', models.CharField(max_length=10, null=True)),
                ('successor_profit_center', models.CharField(max_length=30, null=True)),
                ('country_key', models.CharField(max_length=10, null=True)),
                ('title', models.CharField(max_length=30, null=True)),
                ('name1', models.CharField(max_length=30, null=True)),
                ('name2', models.CharField(max_length=30, null=True)),
                ('name3', models.CharField(max_length=30, null=True)),
                ('name4', models.CharField(max_length=30, null=True)),
                ('city', models.CharField(max_length=10, null=True)),
                ('district', models.CharField(max_length=30, null=True)),
                ('street', models.CharField(max_length=30, null=True)),
                ('po_box', models.CharField(max_length=10, null=True)),
                ('postal_code', models.CharField(max_length=30, null=True)),
                ('p_o_box_costal_code', models.CharField(max_length=30, null=True)),
                ('language_key', models.CharField(max_length=10, null=True)),
                ('telebox_number', models.CharField(max_length=30, null=True)),
                ('telephone1', models.CharField(max_length=30, null=True)),
                ('telephone2', models.CharField(max_length=30, null=True)),
                ('fax_number', models.CharField(max_length=30, null=True)),
                ('teletex_number', models.CharField(max_length=30, null=True)),
                ('telex_number', models.CharField(max_length=30, null=True)),
                ('data_line', models.CharField(max_length=30, null=True)),
                ('printer_name', models.CharField(max_length=30, null=True)),
                ('hierarchy_area', models.CharField(max_length=30, null=True)),
                ('company_code', models.CharField(max_length=30, null=True)),
                ('joint_venture', models.CharField(max_length=30, null=True)),
                ('recovery_indicator', models.CharField(max_length=30, null=True)),
                ('equity_type', models.CharField(max_length=30, null=True)),
                ('tax_jurisdiction', models.CharField(max_length=30, null=True)),
                ('region', models.CharField(max_length=30, null=True)),
                ('usage', models.CharField(max_length=30, null=True)),
                ('application', models.CharField(max_length=30, null=True)),
                ('procedure', models.CharField(max_length=30, null=True)),
                ('logical_system', models.CharField(max_length=30, null=True)),
                ('lock_indicator', models.CharField(max_length=30, null=True)),
                ('prctr_formula_planning_template', models.CharField(max_length=30, null=True)),
                ('segment', models.CharField(max_length=30, null=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('long_text', models.CharField(max_length=100, null=True)),
                ('profit_center_short_text_for_matchcode', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SE16N_T001L',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(null=True)),
                ('week', models.IntegerField(null=True)),
                ('uploaded_by', models.IntegerField()),
                ('uploaded_at', models.DateTimeField()),
                ('division', models.IntegerField(null=True)),
                ('store', models.IntegerField(null=True)),
                ('descr_of_storage_loc', models.CharField(max_length=100, null=True)),
                ('store_level_deletion_indicator', models.CharField(max_length=20, null=True)),
                ('negative_inventory', models.CharField(max_length=20, null=True)),
                ('fix_stk_theo', models.CharField(max_length=20, null=True)),
                ('mrp_code', models.FloatField(null=True)),
                ('authorization_check', models.CharField(max_length=20, null=True)),
                ('stor_resource', models.CharField(max_length=20, null=True)),
                ('management_missing_units', models.CharField(max_length=20, null=True)),
                ('partner_store', models.CharField(max_length=20, null=True)),
                ('sales_organization', models.CharField(max_length=20, null=True)),
                ('distribution_channel', models.CharField(max_length=20, null=True)),
                ('shipping_point_receiving_pt', models.CharField(max_length=20, null=True)),
                ('vendor', models.CharField(max_length=20, null=True)),
                ('customer', models.CharField(max_length=20, null=True)),
                ('business_system_of_mes', models.CharField(max_length=20, null=True)),
                ('inventory_management_type', models.CharField(max_length=20, null=True)),
                ('license_number', models.CharField(max_length=20, null=True)),
                ('in_transit_assignment', models.CharField(max_length=20, null=True)),
                ('tank_assgn', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SE16N_T024',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(null=True)),
                ('week', models.IntegerField(null=True)),
                ('uploaded_by', models.IntegerField()),
                ('uploaded_at', models.DateTimeField()),
                ('purchasing_group', models.CharField(max_length=20, null=True)),
                ('description_p_group', models.CharField(max_length=20, null=True)),
                ('tel_no_purch_group', models.CharField(max_length=20, null=True)),
                ('output_device', models.CharField(max_length=20, null=True)),
                ('fax_number', models.CharField(max_length=20, null=True)),
                ('telephone', models.CharField(max_length=20, null=True)),
                ('extension', models.CharField(max_length=20, null=True)),
                ('e_mail_address', models.CharField(max_length=50, null=True)),
                ('user_name', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock_transit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(null=True)),
                ('week', models.IntegerField(null=True)),
                ('uploaded_by', models.IntegerField(null=True)),
                ('uploaded_at', models.DateTimeField(null=True)),
                ('pExp', models.CharField(max_length=30, null=True)),
                ('taken_plant', models.CharField(max_length=30, null=True)),
                ('transfer_code', models.CharField(max_length=30, null=True)),
                ('poscde', models.CharField(max_length=30, null=True)),
                ('tLvr', models.CharField(max_length=30, null=True)),
                ('actual_sm', models.CharField(max_length=30, null=True)),
                ('delivery', models.CharField(max_length=30, null=True)),
                ('item', models.IntegerField(null=True)),
                ('num_picking_UUID', models.IntegerField(null=True)),
                ('num_parcel', models.CharField(max_length=30, null=True)),
                ('material', models.CharField(max_length=30, null=True)),
                ('delivery_qty', models.FloatField(null=True)),
                ('uq', models.CharField(max_length=30, null=True)),
                ('qty_delivered', models.IntegerField(null=True)),
                ('qty_received', models.IntegerField(null=True)),
                ('not_received', models.CharField(max_length=30, null=True)),
                ('customer_order', models.CharField(max_length=30, null=True)),
                ('of_art_description', models.CharField(max_length=30, null=True)),
                ('msn', models.IntegerField(null=True)),
                ('appro_Special', models.CharField(max_length=30, null=True)),
                ('comment', models.CharField(max_length=30, null=True)),
                ('n_of', models.CharField(max_length=30, null=True)),
                ('article_of', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ZMM_CARNET_CDE_IS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(null=True)),
                ('week', models.IntegerField(null=True)),
                ('uploaded_by', models.IntegerField(null=True)),
                ('uploaded_at', models.DateTimeField()),
                ('request_no', models.CharField(max_length=30, null=True)),
                ('division', models.IntegerField(null=True)),
                ('store', models.IntegerField(null=True)),
                ('purchase_document', models.CharField(max_length=30, null=True)),
                ('poste1', models.CharField(max_length=30, null=True)),
                ('due_date', models.CharField(max_length=20, null=True)),
                ('vendor', models.CharField(max_length=50, null=True)),
                ('vendor_name', models.CharField(max_length=50, null=True)),
                ('material', models.CharField(max_length=50, null=True)),
                ('designation_add_material', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('transmission_info', models.DateTimeField(null=True)),
                ('validated_by', models.CharField(max_length=50, null=True)),
                ('priority', models.CharField(max_length=50, null=True)),
                ('quantity', models.FloatField(null=True)),
                ('quantity_to_receive', models.FloatField(null=True)),
                ('date_of_purchase', models.DateTimeField(null=True)),
                ('desired_date', models.DateTimeField(null=True)),
                ('original_delivery_date', models.DateTimeField(null=True)),
                ('contractual_delivery_date', models.DateTimeField(null=True)),
                ('validated_delivery_date', models.DateTimeField(null=True)),
                ('confirmed_quantity', models.FloatField(null=True)),
                ('comment', models.CharField(max_length=500, null=True)),
                ('expected_stock_week_w', models.FloatField(null=True)),
                ('expected_stock_week_w_1', models.FloatField(null=True)),
                ('expected_stock_week_w_2', models.FloatField(null=True)),
                ('expected_stock_week_w_3', models.FloatField(null=True)),
                ('expected_stock_week_w_4', models.FloatField(null=True)),
                ('expected_stock_week_w_5', models.FloatField(null=True)),
                ('expected_stock_week_w_6', models.FloatField(null=True)),
                ('expected_stock_week_w_7', models.FloatField(null=True)),
                ('expected_stock_week_w_8', models.FloatField(null=True)),
                ('expected_stock_week_w_9', models.FloatField(null=True)),
                ('expected_stock_week_w_10', models.FloatField(null=True)),
                ('expected_stock_week_w_11', models.FloatField(null=True)),
                ('expected_stock_week_w_12', models.FloatField(null=True)),
                ('confirmation', models.CharField(max_length=30, null=True)),
                ('estimated_delivery_time', models.CharField(max_length=20, null=True)),
                ('comment_vendor', models.CharField(max_length=500, null=True)),
                ('element_otp', models.CharField(max_length=30, null=True)),
                ('business_document', models.CharField(max_length=10, null=True)),
                ('poste2', models.CharField(max_length=20, null=True)),
                ('need_number', models.CharField(max_length=30, null=True)),
                ('net_price', models.FloatField(null=True)),
                ('currency', models.CharField(max_length=10, null=True)),
                ('price_basis', models.CharField(max_length=20, null=True)),
                ('price_unit', models.CharField(max_length=10, null=True)),
                ('net_order_value', models.FloatField(null=True)),
                ('purchasing_document_type', models.CharField(max_length=10, null=True)),
                ('exception_message_number', models.CharField(max_length=20, null=True)),
                ('exception_message', models.CharField(max_length=50, null=True)),
                ('purchasing_group', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ZPP_MD_Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(null=True)),
                ('week', models.IntegerField(null=True)),
                ('uploaded_by', models.IntegerField(null=True)),
                ('uploaded_at', models.DateTimeField(null=True)),
                ('division', models.IntegerField(null=True)),
                ('material', models.CharField(max_length=30, null=True)),
                ('plan_date', models.DateTimeField(null=True)),
                ('mrp_element', models.CharField(max_length=30, null=True)),
                ('data_for_planning_element', models.CharField(max_length=30, null=True)),
                ('action_message', models.CharField(max_length=30, null=True)),
                ('Input_need', models.CharField(max_length=30, null=True)),
                ('available_quantity', models.CharField(max_length=30, null=True)),
                ('reorder_date', models.DateTimeField(null=True)),
                ('vendor', models.CharField(max_length=30, null=True)),
                ('customer', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=30, null=True)),
                ('division', models.IntegerField(null=True)),
                ('mrp_area', models.CharField(max_length=30, null=True)),
                ('profit_center', models.CharField(max_length=30, null=True)),
                ('purchase_group_designation', models.CharField(max_length=30, null=True)),
                ('scope_allocation', models.CharField(max_length=30, null=True)),
                ('allocated_supplier', models.CharField(max_length=30, null=True)),
                ('planned_delivery_time', models.CharField(max_length=30, null=True)),
                ('material_type', models.CharField(max_length=30, null=True)),
                ('material_status', models.FloatField(null=True)),
                ('special_procurement_type', models.FloatField(null=True)),
                ('planification_type', models.CharField(max_length=30, null=True)),
                ('lot_qm', models.FloatField(null=True)),
                ('stock_in_transit', models.IntegerField(null=True)),
                ('package_number', models.CharField(max_length=30, null=True)),
                ('warehouse_stock', models.FloatField(null=True)),
                ('workshop_stock', models.FloatField(null=True)),
                ('stock_zpush', models.FloatField(null=True)),
                ('stock_quality', models.FloatField(null=True)),
                ('other_stocks', models.FloatField(null=True)),
                ('stock_in_supply_division', models.FloatField(null=True)),
                ('core_status', models.CharField(default='To do', max_length=30, null=True)),
                ('core_creation', models.TextField(null=True)),
                ('core_comment', models.TextField(null=True)),
                ('ongoing_po', models.CharField(max_length=30, null=True)),
                ('confirmed_delivery_date', models.DateTimeField(null=True)),
                ('quantity_to_receive', models.FloatField(null=True)),
                ('procurement_agent', models.CharField(max_length=50, null=True)),
                ('po_supplier', models.CharField(max_length=50, null=True)),
                ('date_of_missing', models.DateTimeField(null=True)),
                ('missing_status', models.CharField(max_length=30, null=True)),
                ('action', models.CharField(max_length=30, null=True)),
                ('comment', models.CharField(max_length=30, null=True)),
                ('action_status', models.CharField(max_length=30, null=True)),
                ('needs_in_the_past', models.FloatField(null=True)),
                ('backlog_p_qty', models.FloatField(null=True)),
                ('coverage_time', models.IntegerField(null=True)),
                ('week', models.FloatField(null=True)),
                ('week_x', models.FloatField(null=True)),
                ('core', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shortage.core')),
            ],
        ),
        migrations.CreateModel(
            name='CoreHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField()),
                ('created_by', models.IntegerField(default=1)),
                ('comment', models.TextField(null=True)),
                ('action', models.CharField(max_length=30, null=True)),
                ('core', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shortage.core')),
            ],
        ),
    ]
