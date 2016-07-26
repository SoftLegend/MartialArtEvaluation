//const int PIN1 = A1; // Pin connected to FSR/resistor divider
//const int PIN2 = A2; // Pin connected to FSR/resistor divider
//const int PIN3 = A3; // Pin connected to FSR/resistor divider
//const int PIN4 = A4; // Pin connected to FSR/resistor divider

// Measure the voltage at 5V and resistance of your 3.3k resistor, and enter
// their value's below:
const float VCC = 4.98; // Measured voltage of Ardunio 5V line
const float R_DIV = 3230.0; // Measured resistance of 3.3k resistor

float process(float inputADC)
{
  // If the FSR has no pressure, the resistance will be
  // near infinite. So the voltage should be near 0.
  if (inputADC == 0) // If the analog reading is non-zero
    return 0.0;
  
  // Use ADC reading to calculate voltage:
  float fsrV = inputADC * VCC / 1023.0;
  // Use voltage and static resistor value to
  // calculate FSR resistance:
  float fsrR = R_DIV * (VCC / fsrV - 1.0);
  //Serial.println("Resistance: " + String(fsrR) + " ohms");
  // Guesstimate force based on slopes in figure 3 of
  // FSR datasheet:
  float force;
  float fsrG = 1.0 / fsrR; // Calculate conductance
  // Break parabolic curve down into two linear slopes:
  if (fsrR <= 600)
    force = (fsrG - 0.00075) / 0.00000032639;
  else
    force =  fsrG / 0.000000642857;  
    
  return force;
}

void setup()
{
  Serial.begin(9600);
  pinMode(PIN1, INPUT);
  pinMode(PIN2, INPUT);
  pinMode(PIN3, INPUT);
  pinMode(PIN4, INPUT);
}

void loop()
{
  int fsrADC1 = analogRead(A1);
  int fsrADC2 = analogRead(A3);
  int fsrADC3 = analogRead(A4);
  int fsrADC4 = analogRead(A2);
  
  float force1 = process(fsrADC1);
  float force2 = process(fsrADC2);
  float force3 = process(fsrADC3);
  float force4 = process(fsrADC4);
  
  //Serial.println(fsrADC);
  if ((force1 + force2 + force3 + force4) != 0) 
  {
    char sForce1[10];
    char sForce2[10];
    char sForce3[10];
    char sForce4[10];

    dtostrf(force1, 7, 3, sForce1);
    dtostrf(force2, 7, 3, sForce2);
    dtostrf(force3, 7, 3, sForce3);
    dtostrf(force4, 7, 3, sForce4);

    // DEBUG prints...
    //Serial.println(String("0   ") + String(sForce1));
    //Serial.println(String("1   ") + String(sForce2));
    //Serial.println(String("2   ") + String(sForce3));
    //Serial.println(String("3   ") + String(sForce4));

    // Max force
    /*float maxForce = force1;
    if (force2 > maxForce)
      maxForce = force2;
    if (force3 > maxForce)
      maxForce = force3;
    if (force4 > maxForce)
      maxForce = force4;*/
    //Serial.println(maxForce);
    
    float totalForce = force1 + force2 + force3 + force4;
    Serial.println(totalForce);
    delay(50);
    //delay(1000);
  }
  else
  {
    Serial.println(0.0);
    // No pressure detected
  }
}
