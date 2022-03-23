double peso;


void setup() {
  Serial.begin(9600);
  pinMode(A1,INPUT);
}

void loop() {
  peso = analogRead(A1);
  Serial.print(" El peso es: ");
  Serial.println(peso);
  delay(100);
}
