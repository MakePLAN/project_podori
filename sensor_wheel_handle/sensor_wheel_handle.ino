#include <Adafruit_Sensor.h>
#include <Wire.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include <HCSR04.h>



/* Set the delay between fresh samples */
#define BNO055_SAMPLERATE_DELAY_MS (100)

#define leftBuzzerPin 7
#define rightBuzzerPin 8
int buzzer = 0;
int shit;


Adafruit_BNO055 bno = Adafruit_BNO055(55);
UltraSonicDistanceSensor distanceSensor(9, 10);

/**************************************************************************/
/*
    Displays some basic information on this sensor from the unified
    sensor API sensor_t type (see Adafruit_Sensor for more information)
*/
/**************************************************************************/
void displaySensorDetails(void)
{
  sensor_t sensor;
  bno.getSensor(&sensor);
}

/**************************************************************************/
/*
    Display some basic info about the sensor status
*/
/**************************************************************************/
void displaySensorStatus(void)
{
  /* Get the system status values (mostly for debugging purposes) */
  uint8_t system_status, self_test_results, system_error;
  system_status = self_test_results = system_error = 0;
  bno.getSystemStatus(&system_status, &self_test_results, &system_error);
}
/**************************************************************************/
/*
    Display sensor calibration status
*/
/**************************************************************************/
void displayCalStatus(void)
{
  /* Get the four calibration values (0..3) */
  /* Any sensor data reporting 0 should be ignored, */
  /* 3 means 'fully calibrated" */
  uint8_t system, gyro, accel, mag;
  system = gyro = accel = mag = 0;
  bno.getCalibration(&system, &gyro, &accel, &mag);

}

/**************************************************************************/
/*
    Arduino setup function (automatically called at startup)
*/
/**************************************************************************/
void setup(void)
{
  Serial.begin(9600);
  /* Initialise the sensor */
  if(!bno.begin())
  {
    while(1);
  }

  delay(1000);

  /* Display some basic information on this sensor */
  displaySensorDetails();

  /* Optional: Display current status */
  displaySensorStatus();

  bno.setExtCrystalUse(true);

  pinMode(leftBuzzerPin, OUTPUT);
  pinMode(rightBuzzerPin, OUTPUT);
}

int displayTurn(float x){
  int state = 0;
  if(x < 330 && x > 300){
    state = 1;
    return 2;
  }
  else if(x < 300 && x > 270){
    state = 2;
    return 1;
  }
  else if(x > 20  && x < 65){
    state = -1;
    return 4;
  }
  else if(x > 65 && x < 100){
    state = -2;
    return 3;
  }
  else{
    state = 0;
    return 0;
  }
   
}

/**************************************************************************/
/*
    Arduino loop function, called once 'setup' is complete (your own code
    should go here)
*/
/**************************************************************************/
void loop(void)
{
  /* Get a new sensor event */
  sensors_event_t event;
  bno.getEvent(&event);
  String state = "";

  /* Display the floating point data */

  state += displayTurn(event.orientation.x);

    float distance = distanceSensor.measureDistanceCm();
    if(distance > 7.5 || distance == -1){
       state += 5;
    }
    else if(distance < 4.3 && distance > 0){
      state += 6;
    }
    else{
      state += 7;
    }

    Serial.println(state);
  
  /* Optional: Display calibration status */
  displayCalStatus();

  /* Optional: Display sensor status (debug only) */
  displaySensorStatus();


  /* Wait the specified delay before requesting nex data */
  delay(BNO055_SAMPLERATE_DELAY_MS);
  BuzzerHelper2();
}

void BuzzerHelper2(){
  while (Serial.available() > 0) {
    // 0-none 1-left 2-right
    int shit = Serial.read() - 48;
    if (shit == 0 || shit == 1 || shit == 2){
      buzzer = shit;
    }
  }
  if (buzzer == 0) {
    digitalWrite(leftBuzzerPin, LOW);
    digitalWrite(rightBuzzerPin, LOW);
  } else if (buzzer == 1) {
    digitalWrite(leftBuzzerPin, HIGH);
    digitalWrite(rightBuzzerPin, LOW);
  } else if (buzzer == 2){
    digitalWrite(leftBuzzerPin, LOW);
    digitalWrite(rightBuzzerPin, HIGH);
  } else {
    digitalWrite(leftBuzzerPin, LOW);
    digitalWrite(rightBuzzerPin, LOW);
  }
}
