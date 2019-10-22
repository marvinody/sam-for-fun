import argparse

from PySSC import PySSC

if __name__ == "__main__":
	ssc = PySSC()
	parser = argparse.ArgumentParser(description='Process some data.')
	parser.add_argument('--system_capacity',type=int, default=4,
                    help='system cap')
	parser.add_argument('--tilt',type=int, default=30,
                    help="tiliness")
	args = parser.parse_args()
	print(args)

	ssc.module_exec_set_print(0)
	data = ssc.data_create()
	ssc.data_set_string( data, b'solar_resource_file', b'/home/batmanuel/Downloads/SAM/solar_resource/phoenix_az_33.450495_-111.983688_psmv3_60_tmy.csv' );
	ssc.data_set_number( data, b'system_capacity', args.system_capacity)
	ssc.data_set_number( data, b'module_type', 0 )
	ssc.data_set_number( data, b'dc_ac_ratio', 1.2000000476837158 )
	ssc.data_set_number( data, b'inv_eff', 96 )
	ssc.data_set_number( data, b'losses', 14.075660705566406 )
	ssc.data_set_number( data, b'array_type', 0 )
	ssc.data_set_number( data, b'tilt',args.tilt )
	ssc.data_set_number( data, b'azimuth', 180 )
	ssc.data_set_number( data, b'gcr', 0.40000000596046448 )
	ssc.data_set_number( data, b'batt_simple_enable', 0 )
	ssc.data_set_number( data, b'adjust:constant', 0 )
	module = ssc.module_create(b'pvwattsv5')
	ssc.module_exec_set_print( 0 );
	if ssc.module_exec(module, data) == 0:
		print ('pvwattsv5 simulation error')
		idx = 1
		msg = ssc.module_log(module, 0)
		while (msg != None):
			print ('	: ' + msg.decode("utf - 8"))
			msg = ssc.module_log(module, idx)
			idx = idx + 1
		SystemExit( "Simulation Error" );
	ssc.module_free(module)
	ssc.data_set_number( data, b'en_belpe', 0 )
	ssc.data_set_array_from_csv( data, b'load', b'/home/batmanuel/code/python/SAM/load.csv');
	ssc.data_set_number( data, b'floor_area', 2000 )
	ssc.data_set_number( data, b'Stories', 2 )
	ssc.data_set_number( data, b'YrBuilt', 1980 )
	ssc.data_set_number( data, b'Retrofits', 0 )
	ssc.data_set_number( data, b'Occupants', 4 )
	Occ_Schedule =[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ];
	ssc.data_set_array( data, b'Occ_Schedule',  Occ_Schedule);
	ssc.data_set_number( data, b'THeat', 68 )
	ssc.data_set_number( data, b'TCool', 76 )
	ssc.data_set_number( data, b'THeatSB', 68 )
	ssc.data_set_number( data, b'TCoolSB', 76 )
	T_Sched =[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ];
	ssc.data_set_array( data, b'T_Sched',  T_Sched);
	ssc.data_set_number( data, b'en_heat', 1 )
	ssc.data_set_number( data, b'en_cool', 1 )
	ssc.data_set_number( data, b'en_fridge', 1 )
	ssc.data_set_number( data, b'en_range', 1 )
	ssc.data_set_number( data, b'en_dish', 1 )
	ssc.data_set_number( data, b'en_wash', 1 )
	ssc.data_set_number( data, b'en_dry', 1 )
	ssc.data_set_number( data, b'en_mels', 1 )
	Monthly_util =[ 725, 630, 665, 795, 1040, 1590, 1925, 1730, 1380, 1080, 635, 715 ];
	ssc.data_set_array( data, b'Monthly_util',  Monthly_util);
	module = ssc.module_create(b'belpe')
	ssc.module_exec_set_print( 0 );
	if ssc.module_exec(module, data) == 0:
		print ('belpe simulation error')
		idx = 1
		msg = ssc.module_log(module, 0)
		while (msg != None):
			print ('	: ' + msg.decode("utf - 8"))
			msg = ssc.module_log(module, idx)
			idx = idx + 1
		SystemExit( "Simulation Error" );
	ssc.module_free(module)
	ssc.data_set_number( data, b'batt_simple_kwh', 10 )
	ssc.data_set_number( data, b'batt_simple_kw', 5 )
	ssc.data_set_number( data, b'batt_simple_chemistry', 1 )
	ssc.data_set_number( data, b'batt_simple_dispatch', 0 )
	ssc.data_set_number( data, b'batt_simple_meter_position', 0 )
	module = ssc.module_create(b'battwatts')
	ssc.module_exec_set_print( 0 );
	if ssc.module_exec(module, data) == 0:
		print ('battwatts simulation error')
		idx = 1
		msg = ssc.module_log(module, 0)
		while (msg != None):
			print ('	: ' + msg.decode("utf - 8"))
			msg = ssc.module_log(module, idx)
			idx = idx + 1
		SystemExit( "Simulation Error" );
	ssc.module_free(module)
	ssc.data_set_number( data, b'analysis_period', 25 )
	ssc.data_set_number( data, b'inflation_rate', 2.5 )
	degradation =[ 0.5 ];
	ssc.data_set_array( data, b'degradation',  degradation);
	load_escalation =[ 0 ];
	ssc.data_set_array( data, b'load_escalation',  load_escalation);
	rate_escalation =[ 0 ];
	ssc.data_set_array( data, b'rate_escalation',  rate_escalation);
	ssc.data_set_number( data, b'ur_metering_option', 0 )
	ssc.data_set_number( data, b'ur_nm_yearend_sell_rate', 0 )
	ssc.data_set_number( data, b'ur_monthly_fixed_charge', 13 )
	ssc.data_set_number( data, b'ur_monthly_min_charge', 0 )
	ssc.data_set_number( data, b'ur_annual_min_charge', 0 )
	ssc.data_set_number( data, b'ur_en_ts_sell_rate', 0 )
	ur_ts_sell_rate =[ 0 ];
	ssc.data_set_array( data, b'ur_ts_sell_rate',  ur_ts_sell_rate);
	ur_ec_sched_weekday = [[ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   2,   2,   2,   2,   3,   3,   3,   3,   3,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   2,   2,   2,   2,   3,   3,   3,   3,   3,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   2,   2,   2,   2,   3,   3,   3,   3,   3,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   2,   2,   2,   2,   3,   3,   3,   3,   3,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   4,   4,   4,   4,   4,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   4,   4,   4,   4,   4,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   4,   4,   4,   4,   4,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   4,   4,   4,   4,   4,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   4,   4,   4,   4,   4,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   4,   4,   4,   4,   4,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   2,   2,   2,   2,   3,   3,   3,   3,   3,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   2,   2,   2,   2,   3,   3,   3,   3,   3,   1,   1,   1,   1 ]];
	ssc.data_set_matrix( data, b'ur_ec_sched_weekday', ur_ec_sched_weekday );
	ur_ec_sched_weekend = [[ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ]];
	ssc.data_set_matrix( data, b'ur_ec_sched_weekend', ur_ec_sched_weekend );
	ur_ec_tou_mat = [[ 1,   1,   9.9999996802856925e+37,   0,   0.12723599374294281,   0 ], [ 2,   1,   9.9999996802856925e+37,   0,   0.050505999475717545,   0 ], [ 3,   1,   9.9999996802856925e+37,   0,   0.24918599426746368,   0 ], [ 4,   1,   9.9999996802856925e+37,   0,   0.26164600253105164,   0 ]];
	ssc.data_set_matrix( data, b'ur_ec_tou_mat', ur_ec_tou_mat );
	ssc.data_set_number( data, b'ur_dc_enable', 1 )
	ur_dc_sched_weekday = [[ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ]];
	ssc.data_set_matrix( data, b'ur_dc_sched_weekday', ur_dc_sched_weekday );
	ur_dc_sched_weekend = [[ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ]];
	ssc.data_set_matrix( data, b'ur_dc_sched_weekend', ur_dc_sched_weekend );
	ur_dc_tou_mat = [[ 1,   1,   9.9999996802856925e+37,   0 ]];
	ssc.data_set_matrix( data, b'ur_dc_tou_mat', ur_dc_tou_mat );
	ur_dc_flat_mat = [[ 0,   1,   9.9999996802856925e+37,   0 ], [ 1,   1,   9.9999996802856925e+37,   0 ], [ 2,   1,   9.9999996802856925e+37,   0 ], [ 3,   1,   9.9999996802856925e+37,   0 ], [ 4,   1,   9.9999996802856925e+37,   0 ], [ 5,   1,   9.9999996802856925e+37,   0 ], [ 6,   1,   9.9999996802856925e+37,   0 ], [ 7,   1,   9.9999996802856925e+37,   0 ], [ 8,   1,   9.9999996802856925e+37,   0 ], [ 9,   1,   9.9999996802856925e+37,   0 ], [ 10,   1,   9.9999996802856925e+37,   0 ], [ 11,   1,   9.9999996802856925e+37,   0 ]];
	ssc.data_set_matrix( data, b'ur_dc_flat_mat', ur_dc_flat_mat );
	module = ssc.module_create(b'utilityrate5')
	ssc.module_exec_set_print( 0 );
	if ssc.module_exec(module, data) == 0:
		print ('utilityrate5 simulation error')
		idx = 1
		msg = ssc.module_log(module, 0)
		while (msg != None):
			print ('	: ' + msg.decode("utf - 8"))
			msg = ssc.module_log(module, idx)
			idx = idx + 1
		SystemExit( "Simulation Error" );
	ssc.module_free(module)
	federal_tax_rate =[ 15 ];
	ssc.data_set_array( data, b'federal_tax_rate',  federal_tax_rate);
	state_tax_rate =[ 7 ];
	ssc.data_set_array( data, b'state_tax_rate',  state_tax_rate);
	ssc.data_set_number( data, b'property_tax_rate', 2 )
	ssc.data_set_number( data, b'prop_tax_cost_assessed_percent', 100 )
	ssc.data_set_number( data, b'prop_tax_assessed_decline', 0 )
	ssc.data_set_number( data, b'real_discount_rate', 6.4000000953674316 )
	ssc.data_set_number( data, b'insurance_rate', 0.5 )
	ssc.data_set_number( data, b'loan_term', 25 )
	ssc.data_set_number( data, b'loan_rate', 5 )
	ssc.data_set_number( data, b'debt_fraction', 100 )
	om_fixed =[ 0 ];
	ssc.data_set_array( data, b'om_fixed',  om_fixed);
	ssc.data_set_number( data, b'om_fixed_escal', 0 )
	om_production =[ 0 ];
	ssc.data_set_array( data, b'om_production',  om_production);
	ssc.data_set_number( data, b'om_production_escal', 0 )
	om_capacity =[ 16 ];
	ssc.data_set_array( data, b'om_capacity',  om_capacity);
	ssc.data_set_number( data, b'om_capacity_escal', 0 )
	om_fuel_cost =[ 0 ];
	ssc.data_set_array( data, b'om_fuel_cost',  om_fuel_cost);
	ssc.data_set_number( data, b'om_fuel_cost_escal', 0 )
	ssc.data_set_number( data, b'itc_fed_amount', 0 )
	ssc.data_set_number( data, b'itc_fed_amount_deprbas_fed', 1 )
	ssc.data_set_number( data, b'itc_fed_amount_deprbas_sta', 1 )
	ssc.data_set_number( data, b'itc_sta_amount', 0 )
	ssc.data_set_number( data, b'itc_sta_amount_deprbas_fed', 0 )
	ssc.data_set_number( data, b'itc_sta_amount_deprbas_sta', 0 )
	ssc.data_set_number( data, b'itc_fed_percent', 30 )
	ssc.data_set_number( data, b'itc_fed_percent_maxvalue', 9.9999996802856925e+37 )
	ssc.data_set_number( data, b'itc_fed_percent_deprbas_fed', 1 )
	ssc.data_set_number( data, b'itc_fed_percent_deprbas_sta', 1 )
	ssc.data_set_number( data, b'itc_sta_percent', 0 )
	ssc.data_set_number( data, b'itc_sta_percent_maxvalue', 9.9999996802856925e+37 )
	ssc.data_set_number( data, b'itc_sta_percent_deprbas_fed', 0 )
	ssc.data_set_number( data, b'itc_sta_percent_deprbas_sta', 0 )
	ptc_fed_amount =[ 0 ];
	ssc.data_set_array( data, b'ptc_fed_amount',  ptc_fed_amount);
	ssc.data_set_number( data, b'ptc_fed_term', 10 )
	ssc.data_set_number( data, b'ptc_fed_escal', 0 )
	ptc_sta_amount =[ 0 ];
	ssc.data_set_array( data, b'ptc_sta_amount',  ptc_sta_amount);
	ssc.data_set_number( data, b'ptc_sta_term', 10 )
	ssc.data_set_number( data, b'ptc_sta_escal', 0 )
	ssc.data_set_number( data, b'ibi_fed_amount', 0 )
	ssc.data_set_number( data, b'ibi_fed_amount_tax_fed', 1 )
	ssc.data_set_number( data, b'ibi_fed_amount_tax_sta', 1 )
	ssc.data_set_number( data, b'ibi_fed_amount_deprbas_fed', 0 )
	ssc.data_set_number( data, b'ibi_fed_amount_deprbas_sta', 0 )
	ssc.data_set_number( data, b'ibi_sta_amount', 0 )
	ssc.data_set_number( data, b'ibi_sta_amount_tax_fed', 1 )
	ssc.data_set_number( data, b'ibi_sta_amount_tax_sta', 1 )
	ssc.data_set_number( data, b'ibi_sta_amount_deprbas_fed', 0 )
	ssc.data_set_number( data, b'ibi_sta_amount_deprbas_sta', 0 )
	ssc.data_set_number( data, b'ibi_uti_amount', 0 )
	ssc.data_set_number( data, b'ibi_uti_amount_tax_fed', 1 )
	ssc.data_set_number( data, b'ibi_uti_amount_tax_sta', 1 )
	ssc.data_set_number( data, b'ibi_uti_amount_deprbas_fed', 0 )
	ssc.data_set_number( data, b'ibi_uti_amount_deprbas_sta', 0 )
	ssc.data_set_number( data, b'ibi_oth_amount', 0 )
	ssc.data_set_number( data, b'ibi_oth_amount_tax_fed', 1 )
	ssc.data_set_number( data, b'ibi_oth_amount_tax_sta', 1 )
	ssc.data_set_number( data, b'ibi_oth_amount_deprbas_fed', 0 )
	ssc.data_set_number( data, b'ibi_oth_amount_deprbas_sta', 0 )
	ssc.data_set_number( data, b'ibi_fed_percent', 0 )
	ssc.data_set_number( data, b'ibi_fed_percent_maxvalue', 9.9999996802856925e+37 )
	ssc.data_set_number( data, b'ibi_fed_percent_tax_fed', 1 )
	ssc.data_set_number( data, b'ibi_fed_percent_tax_sta', 1 )
	ssc.data_set_number( data, b'ibi_fed_percent_deprbas_fed', 0 )
	ssc.data_set_number( data, b'ibi_fed_percent_deprbas_sta', 0 )
	ssc.data_set_number( data, b'ibi_sta_percent', 0 )
	ssc.data_set_number( data, b'ibi_sta_percent_maxvalue', 9.9999996802856925e+37 )
	ssc.data_set_number( data, b'ibi_sta_percent_tax_fed', 1 )
	ssc.data_set_number( data, b'ibi_sta_percent_tax_sta', 1 )
	ssc.data_set_number( data, b'ibi_sta_percent_deprbas_fed', 0 )
	ssc.data_set_number( data, b'ibi_sta_percent_deprbas_sta', 0 )
	ssc.data_set_number( data, b'ibi_uti_percent', 0 )
	ssc.data_set_number( data, b'ibi_uti_percent_maxvalue', 9.9999996802856925e+37 )
	ssc.data_set_number( data, b'ibi_uti_percent_tax_fed', 1 )
	ssc.data_set_number( data, b'ibi_uti_percent_tax_sta', 1 )
	ssc.data_set_number( data, b'ibi_uti_percent_deprbas_fed', 0 )
	ssc.data_set_number( data, b'ibi_uti_percent_deprbas_sta', 0 )
	ssc.data_set_number( data, b'ibi_oth_percent', 0 )
	ssc.data_set_number( data, b'ibi_oth_percent_maxvalue', 9.9999996802856925e+37 )
	ssc.data_set_number( data, b'ibi_oth_percent_tax_fed', 1 )
	ssc.data_set_number( data, b'ibi_oth_percent_tax_sta', 1 )
	ssc.data_set_number( data, b'ibi_oth_percent_deprbas_fed', 0 )
	ssc.data_set_number( data, b'ibi_oth_percent_deprbas_sta', 0 )
	ssc.data_set_number( data, b'cbi_fed_amount', 0 )
	ssc.data_set_number( data, b'cbi_fed_maxvalue', 9.9999996802856925e+37 )
	ssc.data_set_number( data, b'cbi_fed_tax_fed', 1 )
	ssc.data_set_number( data, b'cbi_fed_tax_sta', 1 )
	ssc.data_set_number( data, b'cbi_fed_deprbas_fed', 0 )
	ssc.data_set_number( data, b'cbi_fed_deprbas_sta', 0 )
	ssc.data_set_number( data, b'cbi_sta_amount', 0 )
	ssc.data_set_number( data, b'cbi_sta_maxvalue', 9.9999996802856925e+37 )
	ssc.data_set_number( data, b'cbi_sta_tax_fed', 1 )
	ssc.data_set_number( data, b'cbi_sta_tax_sta', 1 )
	ssc.data_set_number( data, b'cbi_sta_deprbas_fed', 0 )
	ssc.data_set_number( data, b'cbi_sta_deprbas_sta', 0 )
	ssc.data_set_number( data, b'cbi_uti_amount', 0 )
	ssc.data_set_number( data, b'cbi_uti_maxvalue', 9.9999996802856925e+37 )
	ssc.data_set_number( data, b'cbi_uti_tax_fed', 1 )
	ssc.data_set_number( data, b'cbi_uti_tax_sta', 1 )
	ssc.data_set_number( data, b'cbi_uti_deprbas_fed', 0 )
	ssc.data_set_number( data, b'cbi_uti_deprbas_sta', 0 )
	ssc.data_set_number( data, b'cbi_oth_amount', 0 )
	ssc.data_set_number( data, b'cbi_oth_maxvalue', 9.9999996802856925e+37 )
	ssc.data_set_number( data, b'cbi_oth_tax_fed', 1 )
	ssc.data_set_number( data, b'cbi_oth_tax_sta', 1 )
	ssc.data_set_number( data, b'cbi_oth_deprbas_fed', 0 )
	ssc.data_set_number( data, b'cbi_oth_deprbas_sta', 0 )
	pbi_fed_amount =[ 0 ];
	ssc.data_set_array( data, b'pbi_fed_amount',  pbi_fed_amount);
	ssc.data_set_number( data, b'pbi_fed_term', 0 )
	ssc.data_set_number( data, b'pbi_fed_escal', 0 )
	ssc.data_set_number( data, b'pbi_fed_tax_fed', 1 )
	ssc.data_set_number( data, b'pbi_fed_tax_sta', 1 )
	pbi_sta_amount =[ 0 ];
	ssc.data_set_array( data, b'pbi_sta_amount',  pbi_sta_amount);
	ssc.data_set_number( data, b'pbi_sta_term', 0 )
	ssc.data_set_number( data, b'pbi_sta_escal', 0 )
	ssc.data_set_number( data, b'pbi_sta_tax_fed', 1 )
	ssc.data_set_number( data, b'pbi_sta_tax_sta', 1 )
	pbi_uti_amount =[ 0 ];
	ssc.data_set_array( data, b'pbi_uti_amount',  pbi_uti_amount);
	ssc.data_set_number( data, b'pbi_uti_term', 0 )
	ssc.data_set_number( data, b'pbi_uti_escal', 0 )
	ssc.data_set_number( data, b'pbi_uti_tax_fed', 1 )
	ssc.data_set_number( data, b'pbi_uti_tax_sta', 1 )
	pbi_oth_amount =[ 0 ];
	ssc.data_set_array( data, b'pbi_oth_amount',  pbi_oth_amount);
	ssc.data_set_number( data, b'pbi_oth_term', 0 )
	ssc.data_set_number( data, b'pbi_oth_escal', 0 )
	ssc.data_set_number( data, b'pbi_oth_tax_fed', 1 )
	ssc.data_set_number( data, b'pbi_oth_tax_sta', 1 )
	ssc.data_set_number( data, b'battery_per_kWh', 300 )
	ssc.data_set_number( data, b'market', 0 )
	ssc.data_set_number( data, b'mortgage', 1 )
	ssc.data_set_number( data, b'total_installed_cost', 10783.1201171875 )
	ssc.data_set_number( data, b'salvage_percentage', 0 )
	module = ssc.module_create(b'cashloan')
	ssc.module_exec_set_print( 0 );
	if ssc.module_exec(module, data) == 0:
		print ('cashloan simulation error')
		idx = 1
		msg = ssc.module_log(module, 0)
		while (msg != None):
			print ('	: ' + msg.decode("utf - 8"))
			msg = ssc.module_log(module, idx)
			idx = idx + 1
		SystemExit( "Simulation Error" );
	ssc.module_free(module)
	annual_energy = ssc.data_get_number(data, b'annual_energy');
	print ('Annual energy (year 1) = ', annual_energy)
	capacity_factor = ssc.data_get_number(data, b'capacity_factor');
	print ('Capacity factor (year 1) = ', capacity_factor)
	kwh_per_kw = ssc.data_get_number(data, b'kwh_per_kw');
	print ('Energy yield (year 1) = ', kwh_per_kw)
	lcoe_nom = ssc.data_get_number(data, b'lcoe_nom');
	print ('Levelized COE (nominal) = ', lcoe_nom)
	lcoe_real = ssc.data_get_number(data, b'lcoe_real');
	print ('Levelized COE (real) = ', lcoe_real)
	elec_cost_without_system_year1 = ssc.data_get_number(data, b'elec_cost_without_system_year1');
	print ('Electricity bill without system (year 1) = ', elec_cost_without_system_year1)
	elec_cost_with_system_year1 = ssc.data_get_number(data, b'elec_cost_with_system_year1');
	print ('Electricity bill with system (year 1) = ', elec_cost_with_system_year1)
	savings_year1 = ssc.data_get_number(data, b'savings_year1');
	print ('Net savings with system (year 1) = ', savings_year1)
	npv = ssc.data_get_number(data, b'npv');
	print ('Net present value = ', npv)
	payback = ssc.data_get_number(data, b'payback');
	print ('Simple payback period = ', payback)
	discounted_payback = ssc.data_get_number(data, b'discounted_payback');
	print ('Discounted payback period = ', discounted_payback)
	adjusted_installed_cost = ssc.data_get_number(data, b'adjusted_installed_cost');
	print ('Net capital cost = ', adjusted_installed_cost)
	first_cost = ssc.data_get_number(data, b'first_cost');
	print ('Equity = ', first_cost)
	loan_amount = ssc.data_get_number(data, b'loan_amount');
	print ('Debt = ', loan_amount)
	ssc.data_free(data);
