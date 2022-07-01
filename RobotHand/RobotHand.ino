#include <Servo.h>
 
Servo servoThumb;         
Servo servoIndex;         
Servo servoMiddle;
Servo servoRing;
Servo servoPinky;

#define num 5
#define digitPerVal 1
int valsRec [num];
int stringLength = num * digitPerVal + 1; //$00000
int counter = 0;
bool counterStart = false;

String recievedString;

void setup()
{
    Serial.begin(9600);
    servoThumb.attach(4);
    servoIndex.attach(5);
    servoMiddle.attach(6);
    servoRing.attach(7);
    servoPinky.attach(8);

}
void recievedData(){
    while(Serial.available()){
        char c = Serial.read();
        if (c=='$')
        {
            counterStart = true;
        }
        if(counterStart){
            if(counter < stringLength){
                recievedString = String(recievedString+c);
                counter++;
            }
            if(counter>=stringLength){
                for (int i = 0; i < num; i++)
                {
                    int num = (i*digitPerVal) +1;
                    valsRec[i] = recievedString.substring(num, num + digitPerVal).toInt();
                }
                recievedString ="";
                counter = 0;
                counterStart = false;

            }
        }
    }
}
//void allON(){
//  servoThumb.write(120);
//  servoIndex.write(120);
//  servoMiddle.write(120);
//  servoRing.write(120);
//  servoPinky.write(120);
//  }
void loop()
{
    recievedData();
    if(valsRec[0] == 1){servoThumb.write(120);}else{ servoThumb.write(0);}
    if(valsRec[1] == 1){servoIndex.write(120);}else{ servoIndex.write(0);}
    if(valsRec[2] == 1){servoMiddle.write(120);}else{ servoMiddle.write(0);}
    if(valsRec[3] == 1){servoRing.write(120);}else{ servoRing.write(0);}
    if(valsRec[4] == 1){servoPinky.write(120);}else{ servoPinky.write(0);}
    Serial.print(valsRec[0]);
    Serial.print(valsRec[1]);
    Serial.print(valsRec[2]);
    Serial.print(valsRec[3]);
    Serial.print(valsRec[4]);
    Serial.print("\n");
}
