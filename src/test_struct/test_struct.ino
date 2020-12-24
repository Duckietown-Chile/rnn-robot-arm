
struct robot {
  int t1;
  int t2;
  int t3;
};

struct robot mk3 = {0, 0, 0};
int size_robot = sizeof(struct robot);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  blinkLed(500);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(receive(&mk3)) delay(100);
  
  Serial.println(mk3.t1);
  delay(100);
  Serial.println(mk3.t2);
  delay(100);
  Serial.println(mk3.t3);
  delay(100);
}

void blinkLed(int t) {
  digitalWrite(13, HIGH);
  delay(t/2);
  digitalWrite(13, LOW);
  delay(t/2);
  digitalWrite(13, HIGH);
  delay(t);
  digitalWrite(13, LOW);
  delay(t/2);
}

void send (const robot* table)
{
  Serial.write((const char*)table, size_robot);  // 2 bytes.
}

bool receive(robot* table)
{
  //Serial.println(size_robot);
  return (Serial.readBytes((char*)table, size_robot) == size_robot);
}
