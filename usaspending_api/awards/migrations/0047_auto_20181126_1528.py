# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-26 15:28
from __future__ import unicode_literals

from django.db import migrations, models
from usaspending_api.common.helpers.migration_helpers import drop_like_pattern_ops_index


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0046_merge_20181026_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionfabs',
            name='legal_entity_foreign_descr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactionfabs',
            name='submission_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactionfpds',
            name='place_of_perform_country_n',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactionfpds',
            name='place_of_perform_state_nam',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactionfpds',
            name='referenced_idv_agency_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactionfpds',
            name='referenced_multi_or_single',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='award',
            name='base_and_all_options_value',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='The sum of the base_and_all_options_value from associated transactions', max_digits=23, null=True, verbose_name='Base and All Options Value'),
        ),
        migrations.AlterField(
            model_name='award',
            name='data_source',
            field=models.TextField(choices=[('USA', 'USAspending'), ('DBR', 'DATA Act Broker')], help_text='The source of this entry, either Data Broker (DBR) or USASpending (USA)', null=True),
        ),
        migrations.AlterField(
            model_name='award',
            name='non_federal_funding_amount',
            field=models.DecimalField(blank=True, decimal_places=2, help_text="A summation of this award's transactions' non-federal funding amount", max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='award',
            name='potential_total_value_of_award',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='The sum of the potential_value_of_award from associated transactions', max_digits=23, null=True, verbose_name='Potential Total Value of Award'),
        ),
        migrations.AlterField(
            model_name='award',
            name='total_funding_amount',
            field=models.DecimalField(blank=True, decimal_places=2, help_text="A summation of this award's transactions' funding amount", max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='award',
            name='total_obligation',
            field=models.DecimalField(db_index=True, decimal_places=2, help_text='The amount of money the government is obligated to pay for the award', max_digits=23, null=True, verbose_name='Total Obligated'),
        ),
        migrations.AlterField(
            model_name='award',
            name='total_outlay',
            field=models.DecimalField(db_index=True, decimal_places=2, help_text='The total amount of money paid out for this award', max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='award',
            name='total_subaward_amount',
            field=models.DecimalField(decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='award',
            name='total_subsidy_cost',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='The total of the original_loan_subsidy_cost from associated transactions', max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='data_source',
            field=models.TextField(choices=[('USA', 'USAspending'), ('DBR', 'DATA Act Broker')], help_text='The source of this entry, either Data Broker (DBR) or USASpending (USA)', null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='deobligations_recoveries_refunds_of_prior_year_by_award_cpe',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='drv_obligations_incurred_total_by_award',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='gross_outlay_amount_by_award_cpe',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='gross_outlay_amount_by_award_fyb',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='gross_outlays_delivered_orders_paid_total_cpe',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='gross_outlays_delivered_orders_paid_total_fyb',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='gross_outlays_undelivered_orders_prepaid_total_cpe',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='gross_outlays_undelivered_orders_prepaid_total_fyb',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='obligations_delivered_orders_unpaid_total_cpe',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='obligations_delivered_orders_unpaid_total_fyb',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='obligations_incurred_total_by_award_cpe',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='obligations_undelivered_orders_unpaid_total_cpe',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='obligations_undelivered_orders_unpaid_total_fyb',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='transaction_obligated_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='ussgl480100_undelivered_orders_obligations_unpaid_cpe',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='ussgl480100_undelivered_orders_obligations_unpaid_fyb',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='ussgl480200_undelivered_orders_oblig_prepaid_advanced_cpe',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='ussgl480200_undelivered_orders_oblig_prepaid_advanced_fyb',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='ussgl483100_undelivered_orders_oblig_transferred_unpaid_cpe',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='ussgl483200_undeliv_orders_oblig_transferred_prepaid_adv_cpe',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='ussgl487100_down_adj_pri_unpaid_undel_orders_oblig_recov_cpe',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='ussgl487200_down_adj_pri_ppaid_undel_orders_oblig_refund_cpe',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='ussgl488100_upward_adjust_pri_undeliv_order_oblig_unpaid_cpe',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='ussgl488200_up_adjust_pri_undeliv_order_oblig_ppaid_adv_cpe',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='ussgl490100_delivered_orders_obligations_unpaid_cpe',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='ussgl490100_delivered_orders_obligations_unpaid_fyb',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='ussgl490200_delivered_orders_obligations_paid_cpe',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='ussgl490800_authority_outlayed_not_yet_disbursed_cpe',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='ussgl490800_authority_outlayed_not_yet_disbursed_fyb',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='ussgl493100_delivered_orders_oblig_transferred_unpaid_cpe',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='ussgl497100_down_adj_pri_unpaid_deliv_orders_oblig_recov_cpe',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='ussgl497200_down_adj_pri_paid_deliv_orders_oblig_refund_cpe',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='ussgl498100_upward_adjust_pri_deliv_orders_oblig_unpaid_cpe',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='ussgl498200_upward_adjust_pri_deliv_orders_oblig_paid_cpe',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='subaward',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=23),
        ),
        migrations.AlterField(
            model_name='transactionfabs',
            name='afa_generated_unique',
            field=models.TextField(db_index=True, unique=True),
        ),
        # Drop "_like" indexes since we're converting from text to integer.
        migrations.RunPython(
            drop_like_pattern_ops_index('awards', 'transactionfabs', 'published_award_financial_assistance_id')
        ),
        migrations.AlterField(
            model_name='transactionfabs',
            name='published_award_financial_assistance_id',
            field=models.IntegerField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='transactionfabs',
            name='updated_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='airport_authority',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='alaskan_native_owned_corpo',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='alaskan_native_servicing_i',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='american_indian_owned_busi',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='asian_pacific_american_own',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='black_american_owned_busin',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='c1862_land_grant_college',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='c1890_land_grant_college',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='c1994_land_grant_college',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='c8a_program_participant',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='city_local_government',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='community_developed_corpor',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='community_development_corp',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='contracts',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='corporate_entity_not_tax_e',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='corporate_entity_tax_exemp',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='council_of_governments',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='county_local_government',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='detached_award_proc_unique',
            field=models.TextField(null=True, unique=True),
        ),
        # Drop "_like" indexes since we're converting from text to integer.
        migrations.RunPython(
            drop_like_pattern_ops_index('awards', 'transactionfpds', 'detached_award_procurement_id')
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='detached_award_procurement_id',
            field=models.IntegerField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='domestic_shelter',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='dot_certified_disadvantage',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='economically_disadvantaged',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='educational_institution',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='emerging_small_business',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='federal_action_obligation',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='federal_agency',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='federally_funded_research',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='for_profit_organization',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='foreign_government',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='foreign_owned_and_located',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='foundation',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='grants',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='hispanic_american_owned_bu',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='hispanic_servicing_institu',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='historically_black_college',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='historically_underutilized',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='hospital_flag',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='housing_authorities_public',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='indian_tribe_federally_rec',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='inter_municipal_local_gove',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='international_organization',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='interstate_entity',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='joint_venture_economically',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='joint_venture_women_owned',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='labor_surplus_area_firm',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='limited_liability_corporat',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='local_government_owned',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='manufacturer_of_goods',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='minority_institution',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='minority_owned_business',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='municipality_local_governm',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='native_american_owned_busi',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='native_hawaiian_owned_busi',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='native_hawaiian_servicing',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='nonprofit_organization',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='other_minority_owned_busin',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='other_not_for_profit_organ',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='partnership_or_limited_lia',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='planning_commission',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='port_authority',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='private_university_or_coll',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='receives_contracts_and_gra',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='sba_certified_8_a_joint_ve',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='school_district_local_gove',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='school_of_forestry',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='self_certified_small_disad',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='service_disabled_veteran_o',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='small_agricultural_coopera',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='small_business_competitive',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='small_disadvantaged_busine',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='sole_proprietorship',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='state_controlled_instituti',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='subchapter_s_corporation',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='subcontinent_asian_asian_i',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='the_ability_one_program',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='township_local_government',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='transit_authority',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='tribal_college',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='tribally_owned_business',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='updated_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='us_federal_government',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='us_government_entity',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='us_local_government',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='us_state_government',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='us_tribal_government',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='veteran_owned_business',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='veterinary_college',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='veterinary_hospital',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='woman_owned_business',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionfpds',
            name='women_owned_small_business',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='transactionnormalized',
            name='drv_award_transaction_usaspend',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='transactionnormalized',
            name='drv_current_total_award_value_amount_adjustment',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='transactionnormalized',
            name='drv_potential_total_award_value_amount_adjustment',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='transactionnormalized',
            name='federal_action_obligation',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='The obligation of the federal government for this transaction', max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='transactionnormalized',
            name='funding_amount',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Assistance data variable.  non_federal_funding_amount + federal_action_obligation', max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='transactionnormalized',
            name='non_federal_funding_amount',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Assistance Data variable.', max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='transactionnormalized',
            name='original_loan_subsidy_cost',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='The original_loan_subsidy_cost for loan type transactions', max_digits=23, null=True),
        ),
        migrations.AddIndex(
            model_name='award',
            index=models.Index(fields=['-update_date'], name='awards_update_date_desc_idx'),
        ),
        migrations.AddIndex(
            model_name='award',
            index=models.Index(fields=['generated_unique_award_id'], name='award_unique_id'),
        ),
        # For whatever reason, Django refuses to update these OneToOneFields itself, so we'll
        # do it the "hard" way.
        migrations.RunSQL(
            sql='alter table only "transaction_fabs" alter column "transaction_id" type bigint',
            reverse_sql='alter table only "transaction_fabs" alter column "transaction_id" type int'
        ),
        migrations.RunSQL(
            sql='alter table only "transaction_fpds" alter column "transaction_id" type bigint',
            reverse_sql='alter table only "transaction_fpds" alter column "transaction_id" type int'
        ),
        # Rename some sequences to match database.
        migrations.RunSQL(
            sql='alter sequence "awards_id_seq" rename to "award_id_seq"',
            reverse_sql='alter sequence "award_id_seq" rename to "awards_id_seq"'
        ),
        migrations.RunSQL(
            sql='alter sequence "transaction_normalized_id_seq" rename to "tx_norm_id_seq"',
            reverse_sql='alter sequence "tx_norm_id_seq" rename to "transaction_normalized_id_seq"'
        ),
    ]
