#!/usr/bin/env python
# coding: utf-8

# In[ ]:


package SeleniumStart;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class WebdriverBasics {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		System.setProperty("webdriver.chrome.driver","C:\\Selenium+java\\Chromedriver\\chromedriver");
		WebDriver driver = new ChromeDriver();
		
		driver.get("http://demo.guru99.com/insurance/v1/index.php");
		
		WebElement email = driver.findElement(By.id("email"));
		email.sendKeys("tejasbhad74@gmail.com");
		
		WebElement password =driver.findElement(By.id("email"));
	 email.sendKeys("Autommation");

	}

}

