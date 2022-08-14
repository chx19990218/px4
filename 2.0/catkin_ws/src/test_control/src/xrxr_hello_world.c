



#include <px4_platform_common/log.h>
#include <px4_platform_common/posix.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <poll.h>
#include <math.h>

//#include <systemlib/err.h>
//#include <drivers/drv_hrt.h>

#include <uORB/uORB.h>
//#include <uORB/topics/debug_key_value.h>




__EXPORT int xrxr_hello_world_main(int argc, char *argv[]);

#include <uORB/topics/vehicle_local_position.h>
void receiveAndPrintVLP(void)
{
	struct vehicle_local_position_s _local_pos;
	int _local_pos_sub = orb_subscribe(ORB_ID(vehicle_local_position));
	px4_pollfd_struct_t fds[1];
	fds[0].fd = _local_pos_sub;
	fds[0].events = POLLIN;
	for(int i = 0; i < 100; i++)
	{
		int poll_ret = px4_poll(fds, 1, 1000);//wait for message for 1000 ms (1 second)
		if (fds[0].revents & POLLIN && poll_ret != -1)
		{
			orb_copy(ORB_ID(vehicle_local_position), _local_pos_sub, &_local_pos);//copy data into local buffer
			printf("%f\t%f\t%f\n", (double)_local_pos.ax, (double)_local_pos.ay, (double)_local_pos.az);
		}

	}
	orb_unsubscribe(_local_pos_sub);
}
void publishVLP(void)
{
	//advertise named debug value
	struct vehicle_local_position_s lpos;
	// generate vehicle local position data
	uint64_t timestamp_us = hrt_absolute_time();
	lpos.timestamp_sample = timestamp_us;
	// Position of body origin in local NED frame
	lpos.x = 0;
	lpos.y = 0;
	lpos.z = 0;
	// Velocity of body origin in local NED frame (m/s)
	lpos.vx = 0;
	lpos.vy = 0;
	lpos.vz = 0;
	// vertical position time derivative (m/s)
	lpos.z_deriv = 0;
	// Acceleration of body origin in local frame
	lpos.ax = 0;
	lpos.ay = 0;
	lpos.az = 0;
	// TODO: better status reporting
	lpos.xy_valid = 1;
	lpos.z_valid = 1;
	lpos.v_xy_valid = 1;
	lpos.v_z_valid = 1;
	// Position of local NED origin in GPS / WGS84 frame
	lpos.ref_alt = 0;
	lpos.ref_timestamp = timestamp_us;
	lpos.ref_lat = 0; // Reference point latitude in degrees
	lpos.ref_lon = 0; // Reference point longitude in degrees

	lpos.xy_global = 0;
	lpos.z_global = 0;

	lpos.heading_reset_counter = 0;

	lpos.heading = 0;
	lpos.delta_heading = 0;

	lpos.dist_bottom_valid = 0;

	lpos.dist_bottom = 0;
	//uORB::PublicationMulti<vehicle_local_position_s> _local_position_pub;
	orb_advert_t pub_dbg_key = orb_advertise(ORB_ID(vehicle_local_position), &lpos);
	for(int i = 0; i < 100; i++)
	{

		//send one named value

		orb_publish(ORB_ID(vehicle_local_position), pub_dbg_key, &lpos);
		px4_usleep(10000);//10ms
	}
}

#include <uORB/topics/sensor_gps.h>
//	sensor_gps_s			_report_gps_pos{};				///< uORB topic for gps position
//uORB::Subscription		_orb_inject_data_sub{ORB_ID(gps_inject_data)};

#define XRXR_START_LAT 457324710
#define XRXR_START_LOT 1266279384
#define XRXR_START_ALT 123253
void generateGPSdata(void)
{
	struct sensor_gps_s gpsData;
	gpsData.timestamp = hrt_absolute_time();//时间(us)(uint64_t)
	gpsData.time_utc_usec = gpsData.timestamp + (uint64_t)1610025000000000;//UTC时间(us)(uint64_t)
	gpsData.lat = XRXR_START_LAT;	//纬度(degE7)(int32_t)
	gpsData.lon = XRXR_START_LOT;	//经度(degE7)(int32_t)
	gpsData.alt = XRXR_START_ALT;	//海拔(mm)(int32_t)
	gpsData.alt_ellipsoid = XRXR_START_ALT+11670;	//海拔_椭圆面(mm)(int32_t)
	gpsData.s_variance_m_s = 0.62f;	//GPS speed accuracy estimate(m/s)(float)
	gpsData.c_variance_rad = 0.73f;	//GPS course accuracy estimate(rad)(float)
	gpsData.eph = 11.35;		//GPS HDOP horizontal dilution of position. If unknown, set to: 65535(cm)(float)
	gpsData.epv = 11.16;		//GPS VDOP vertical dilution of position. If unknown, set to: 65535(cm)(float)
	gpsData.hdop = 1.7;		//精度因子(float)
	gpsData.vdop = 1.7;		//精度因子(float)
	gpsData.noise_per_ms = 99;	//GPS noise per millisecond(int32_t)
	gpsData.jamming_indicator = 0;	//indicates jamming is occurring(int32_t)
	gpsData.vel_m_s = 0;		//GPS ground speed(m/s)(float)
	gpsData.vel_n_m_s = 0;		//GPS North velocity(m/s)(float)
	gpsData.vel_e_m_s = 0;		//GPS East velocity(m/s)(float)
	gpsData.vel_d_m_s = 0;		//GPS Down velocity(m/s)(float)
	gpsData.cog_rad = 2.999904;		//Course over ground (NOT heading, but direction of movement), -PI..PI, (radians)(float)
	gpsData.timestamp_time_relative = 0;//timestamp + timestamp_time_relative = Time of the UTC timestamp since system start(ms)(int32_t)
	gpsData.heading = 1.0f/0.0f;//heading angle of XYZ body frame rel to NED. Set to NaN if not available and updated(float)
	gpsData.heading_offset = 0;//?(float)
	gpsData.fix_type = 3;//0-1: no fix, 2: 2D fix, 3: 3D fix, 4: RTCM code differential, 5: Real-Time Kinematic, float, 6: Real-Time Kinematic, fixed, 8: Extrapolated(uint8_t)
	gpsData.vel_ned_valid = 1;//True if NED velocity is valid(bool)
	gpsData.satellites_used = 12;//?(uint8_t)
	//gpsData._padding0[0] = 0;//required for logger(uint8_t)
	orb_advert_t pub_sensor_gps = orb_advertise(ORB_ID(sensor_gps), &gpsData);
	for(int i = 0; i < 100000; i++)//10Hz,100sec
	{
		//gpsData.lat = XRXR_START_LAT + 1e6*sin(i/100.0);	//纬度(degE7)(int32_t)
		//gpsData.lon = XRXR_START_LOT + 1e6*cos(i/100.0);	//经度(degE7)(int32_t)
		//gpsData.alt = XRXR_START_ALT;	//海拔(mm)(int32_t)
		//gpsData.alt_ellipsoid = XRXR_START_ALT+11670;	//海拔_椭圆面(mm)(int32_t)
		gpsData.timestamp = hrt_absolute_time();//时间(us)(uint64_t)
		gpsData.time_utc_usec = gpsData.timestamp + (uint64_t)1608336000000000;//UTC时间(us)(uint64_t)
		orb_publish(ORB_ID(sensor_gps), pub_sensor_gps, &gpsData);
		px4_usleep(100000);//100ms,10Hz
		if(i%10 == 0) printf("%d\t%f\t%f\t%f\r\n", i, ((double)gpsData.lat)*1.0e-9, ((double)gpsData.lon)*1.0e-9, ((double)gpsData.alt));
	}
}
void receiveAndPrintGPS(void)
{
	struct sensor_gps_s gpsData;
	int _gps_sub = orb_subscribe(ORB_ID(sensor_gps));
	px4_pollfd_struct_t fds[1];
	fds[0].fd = _gps_sub;
	fds[0].events = POLLIN;
	for(int i = 0; i < 100; i++)
	{
		int poll_ret = px4_poll(fds, 1, 1000);//wait for message for 1000 ms (1 second)
		if (fds[0].revents & POLLIN && poll_ret != -1)
		{
			orb_copy(ORB_ID(sensor_gps), _gps_sub, &gpsData);//copy data into local buffer
			printf("%llu\t%llu\t%d\t%d\t%d\t%d\t%f\t%f\t%f\t%f\t%f\t%f\t%d\t%d\t%f\t%f\t%f\t%f\t%f\t%d\t%f\t%f\t%d\t%d\t%d\n\n\n\n\n",
			gpsData.timestamp, gpsData.time_utc_usec,
			gpsData.lat, gpsData.lon, gpsData.alt, gpsData.alt_ellipsoid,
			(double)gpsData.s_variance_m_s, (double)gpsData.c_variance_rad, (double)gpsData.eph, (double)gpsData.epv, (double)gpsData.hdop, (double)gpsData.vdop,
			gpsData.noise_per_ms, gpsData.jamming_indicator,
			(double)gpsData.vel_m_s, (double)gpsData.vel_n_m_s, (double)gpsData.vel_e_m_s, (double)gpsData.vel_d_m_s, (double)gpsData.cog_rad,
			gpsData.timestamp_time_relative,
			(double)gpsData.heading, (double)gpsData.heading_offset,
			(int)gpsData.fix_type, (int)gpsData.vel_ned_valid, (int)gpsData.satellites_used);
		}
	}
	orb_unsubscribe(_gps_sub);
}
#include <uORB/topics/xrxr_fake_gps.h>
void receiveFakeGPS(void)
{
	struct xrxr_fake_gps_s fakeGpsData;
	int _fakegps_sub = orb_subscribe(ORB_ID(xrxr_fake_gps));
	px4_pollfd_struct_t fds[1];
	fds[0].fd = _fakegps_sub;
	fds[0].events = POLLIN;
	for(int i = 0; i < 100; i++)
	{
		int poll_ret = px4_poll(fds, 1, 1000);//wait for message for 1000 ms (1 second)
		if (fds[0].revents & POLLIN && poll_ret != -1)
		{
			orb_copy(ORB_ID(xrxr_fake_gps), _fakegps_sub, &fakeGpsData);//copy data into local buffer
			printf("%llu\t%llu\t%d\t%d\t%d\t%d\t%f\t%f\t%f\t%f\t%f\t%f\t%d\t%d\t%f\t%f\t%f\t%f\t%f\t%d\t%f\t%f\t%d\t%d\t%d\n\n\n\n\n",
			fakeGpsData.timestamp, fakeGpsData.time_utc_usec,
			fakeGpsData.lat, fakeGpsData.lon, fakeGpsData.alt, fakeGpsData.alt_ellipsoid,
			(double)fakeGpsData.s_variance_m_s, (double)fakeGpsData.c_variance_rad, (double)fakeGpsData.eph, (double)fakeGpsData.epv, (double)fakeGpsData.hdop, (double)fakeGpsData.vdop,
			fakeGpsData.noise_per_ms, fakeGpsData.jamming_indicator,
			(double)fakeGpsData.vel_m_s, (double)fakeGpsData.vel_n_m_s, (double)fakeGpsData.vel_e_m_s, (double)fakeGpsData.vel_d_m_s, (double)fakeGpsData.cog_rad,
			fakeGpsData.timestamp_time_relative,
			(double)fakeGpsData.heading, (double)fakeGpsData.heading_offset,
			(int)fakeGpsData.fix_type, (int)fakeGpsData.vel_ned_valid, (int)fakeGpsData.satellites_used);
		}
	}
	orb_unsubscribe(_fakegps_sub);
}

int xrxr_hello_world_main(int argc, char *argv[])
{
	PX4_INFO("xrxr_hello_world");
	//receiveAndPrintVLP();
	//publishVLP();
	//generateGPSdata();
	//receiveAndPrintGPS();
	receiveFakeGPS();
	return OK;
}
