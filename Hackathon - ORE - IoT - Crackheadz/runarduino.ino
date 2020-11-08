#include<Servo.h>
Servo servo_mot;
int pos;
int c=0;
char flag;

void setup()
{
  pos=0;
  servo_mot.attach(9);  //Servo Motor
  pinMode(13,OUTPUT); //Indicator LED
  pinMode(7,INPUT); //IR Sensor
  Serial.begin(9600);
}
void loop()
{
  if (digitalRead(3)== LOW)
  {
    digitalWrite(13,HIGH);
    delay(10);
    if(Serial.available()>0)
    {
      Serial.write('1');
      flag=Serial.read();
    }
    if(c==1)
      exit(0);
    else
    {
      if(flag=='1')
      {
        for (pos = 90; pos >= 0; pos -= 1)
        {
          servo_mot.write(pos);
          delay(50);
        }
        delay(3000);
        for (pos = 0; pos <= 90; pos += 1)
        {
          servo_mot.write(pos);  
          delay(50);
        }
      }
      if(flag>0)
        c=c+1;
    }
    }
    else
    {
      digitalWrite(13,LOW);
      Serial.write('0');
      delay(10);
    }
}
