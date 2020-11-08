#include <Servo.h>
Servo servo_mot; //initialiseing the servo
void setup() {   //setting the pinmode connections
 pinMode(7,INPUT);
 servo_mot.attach(13);
 servo_mot.write(0);//intially set the servo  to zero
}

void loop() {
if(digitalRead(7)==LOW)//if the person is in our circle then the digitalreadpin
                        //will produce of HIGH pulse the if became true                      
{
 
  servo_mot.write(0);//initially this will be zero
  delay(500);// making a delay of 0.5 sec
  servo_mot.write(90); //then servo rotates for an angle 90
  delay(500); // making delay
}
 else  //the person is not in our circle
 {
  servo_mot.write(0); // servo is at zero angle.
 }
  
}
