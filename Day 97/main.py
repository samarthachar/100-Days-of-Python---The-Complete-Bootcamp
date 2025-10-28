from datetime import datetime, timedelta

from selenium import webdriver
import os
from dotenv import load_dotenv
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()
SCHOOL_ID = os.getenv("SCHOOL_ID")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

class BromComScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()
    def login(self):
        self.driver.get("https://www.bromcomvle.com/")
        time.sleep(10)

        school_id_field = self.driver.find_element(By.ID, "schoolid")
        school_id_field.send_keys(SCHOOL_ID)

        username_field = self.driver.find_element(By.ID, "username")
        username_field.send_keys(USERNAME)

        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(PASSWORD)

        wait = WebDriverWait(self.driver, 5)
        login_button = wait.until(EC.element_to_be_clickable((By.ID, "LoginButton")))
        login_button.click()
        time.sleep(60)

    def get_timetable(self):

        wait = WebDriverWait(self.driver, 5)
        timetable_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-menuname="Timetable"]')))
        timetable_button.click()
        time.sleep(10)

        table = self.driver.find_element(By.ID, "Timetable")
        thead = table.find_element(By.TAG_NAME, "thead")
        headers = thead.find_elements(By.TAG_NAME, "th")
        days = [header.text.split("\n")[0] for header in headers]

        schedule = {day: [] for day in days}

        tbody = table.find_element(By.TAG_NAME, "tbody")
        rows = tbody.find_elements(By.TAG_NAME, "tr")

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            for i, cell in enumerate(cells):
                day = days[i]
                text = cell.text.strip().upper()

                # Handle BREAK or LUNCH
                if text in ["BREAK", "LUNCH"]:
                    schedule[day].append({"period": text})
                    continue


                try:
                    lines = cell.text.strip().split("\n")

                    if len(lines) < 4:
                        print(f"Skipping malformed cell on {day}: {lines}")
                        continue

                    class_code = lines[0]
                    room = lines[1]
                    subject = lines[2]
                    teacher = lines[3] if len(lines) > 3 else None


                    entry = {
                        "period":str(len(schedule[day]) + 1),
                        "class": class_code or None,
                        "room": room or None,
                        "subject": subject,
                        "teacher": teacher
                    }

                    schedule[day].append(entry)

                except Exception as e:
                    print(f"Error in cell for {day}: {e}")
                    continue
        return schedule

    def get_homework(self):
        wait = WebDriverWait(self.driver, 5)
        homework_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-menuname="Homework"]')))
        homework_button.click()
        time.sleep(5)

        table = self.driver.find_element(By.ID, "HomeworkTable")
        rows = table.find_elements(By.TAG_NAME, "tr")

        homeworks = []
        now = datetime.now()
        next_week = now + timedelta(days=7)

        for row in rows:
            try:
                due_text = row.find_element(By.ID, "sp-table-contents-date").text.strip()
                title = row.find_element(By.ID, "sp-table-contents-title").text.strip()
                subject = row.find_elements(By.TAG_NAME, "td")[4].text.strip()
                teacher = row.find_element(By.ID, "sp-table-contents-teacher").text.strip()
                status = row.find_element(By.ID, "sp-table-contents-status").text.strip()

                due_date = datetime.strptime(due_text, "%d/%m/%Y")
                if now <= due_date <= next_week:
                    homeworks.append({
                        "due": due_date,
                        "title": title,
                        "subject": subject,
                        "teacher": teacher,
                        "status": status
                    })

            except Exception as e:
                print(f"Skipping row due to error: {e}")
                continue
        print(homeworks)

bot = BromComScraper()
bot.login()
# timetable = bot.get_timetable()
bot.get_homework()