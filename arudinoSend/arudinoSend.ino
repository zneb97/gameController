
//Pot pin numbers
int pot1 = 0;
int pot2 = 1;
int pot3 = 2;
int pot4 = 3;
int rot = 4;

//Pot offsets
int p1Fix = 0;
int p2Fix = 0;
int p3Fix = 0;
int p4Fix = 0;
int rotFix = 0;

//Button pin number
int button = 8;

void setup() {
  // Make sure the baud rate is the same as in sendReceive.py
  Serial.begin(115200);
  pinMode(button,INPUT);

}

void loop() {
  //Read button
  int state = digitalRead(button);
  
  //Read pots
  int p1 = analogRead(pot1);
  int p2 = analogRead(pot2);
  int p3 = analogRead(pot3);
  int p4 = analogRead(pot4);
  int rot = analogRead(rot)+rotFix;

  //Get positions
  int x = (p1+p1Fix)-(p3+p3Fix);
  int y = (p1+p1Fix)-(p3+p3Fix);
  int z = (p1+p1Fix)-(p3+p3Fix);

  //Send data
  Serial.println( String(x)+"&"+String(y)+"&"+String(z)+"&"+String(rot)+"&"+String(state))

}
