import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time

load_dotenv()

ACCOUNT_EMAIL = os.getenv("ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = os.getenv("ACCOUNT_PASSWORD")

link1 = "https://appbrewery.github.io/gym/"

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)

driver.get(link1)

booked_count = 0
waitlist_count = 0
already_booked_count = 0
processed_classes = []
wait = WebDriverWait(driver, 2)

expected_bookings = booked_count + waitlist_count + already_booked_count
found_bookings = 0
def retry(func):
    try:
        func()
    except:
        retry(func)


def login():




    # Inputs Email and Password into fields
    wait.until(ec.element_to_be_clickable((By.ID, "login-button"))).click()

    password_input = wait.until(ec.presence_of_element_located((By.ID, "password-input")))

    email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
    email_input.clear()


    email_input.send_keys(ACCOUNT_EMAIL)
    email_input.send_keys(Keys.ENTER)

    password_input.clear()

    password_input.send_keys(ACCOUNT_PASSWORD)
    password_input.send_keys(Keys.ENTER)

    driver.find_element(By.ID, "submit-button").click()

    wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

def book_class():

    global booked_count, waitlist_count, already_booked_count, processed_classes
    time.sleep(1)
    class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")



    for card in class_cards:
        day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
        day_title = day_group.find_element(By.TAG_NAME, "h2").text
        if "Tue" in day_title or "Thu" in day_title:
            time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
            if "6:00 PM" in time_text:
                class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
                button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
                class_info = f"{class_name} on {day_title}"
                if "Book Class" in button.text:
                    button.click()
                    print(f"✓ Successfully booked: {class_info}")
                    processed_classes.append(f"[New Booking] {class_info}")
                    booked_count += 1
                elif "Booked" in button.text:
                    print(f"✓ Already booked: {class_info}")
                    processed_classes.append(f"[Booked] {class_info}")
                    already_booked_count += 1
                elif "Join Waitlist" in button.text:
                    button.click()
                    print(f"✓ Joined waitlist for: {class_info}")
                    processed_classes.append(f"[New Waitlist] {class_info}")
                    waitlist_count += 1
                elif "Waitlisted" in button.text:
                    print(f"✓ Already on waitlist: {class_info}")
                    processed_classes.append(f"[Waitlisted] {class_info}")
                    already_booked_count += 1
                else:
                    print(f"⚠️ Unknown button state {button.text}")

    print("\n--- BOOKING SUMMARY ---")
    print(f"Classes booked: {booked_count}")
    print(f"Waitlists joined: {waitlist_count}")
    print(f"Already booked/waitlisted: {already_booked_count}")
    print(f"Total Tuesday & 6pm classes processed: {booked_count + waitlist_count + already_booked_count}")

    wait.until(ec.presence_of_element_located((By.ID, "my-bookings-link"))).click()

def verify():
    global expected_bookings, found_bookings
    try:
        confirmed_booking_cards = wait.until(
            ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[id^="booking-card-"]')))
    except:
        confirmed_booking_cards = []
    try:
        confirmed_waitlist_cards = wait.until(
            ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[id^="waitlist-card-waitlist"]')))
    except:
        confirmed_waitlist_cards = []



    print("--- VERIFICATION RESULTS ---")

    for card in confirmed_booking_cards:
        date = card.find_element(By.CSS_SELECTOR, 'div[class="MyBookings_bookingDetails__QG0l_"] p').text[6:]
        date = date.replace(",", "")
        date_list = date.split()

        for class1 in processed_classes:
            counter = 0
            for each_date in date_list:
                if each_date in class1:
                    counter += 1

            if counter == 3:
                found_bookings += 1
    for card in confirmed_waitlist_cards:
        date = card.find_element(By.CSS_SELECTOR, 'div[class="MyBookings_bookingDetails__QG0l_"] p').text[6:]
        date = date.replace(",", "")
        date_list = date.split()

        for class1 in processed_classes:
            counter = 0
            for each_date in date_list:
                if each_date in class1:
                    counter += 1

            if counter == 3:
                found_bookings += 1



retry(login)
retry(book_class)


print("\n--- DETAILED CLASS LIST ---")
for class_detail in processed_classes:
    print(f"  • {class_detail}")

retry(verify)



print(f"Expected: {expected_bookings} bookings\nFound: {found_bookings}")
if expected_bookings == found_bookings:
    print("SUCCESS: All bookings verified")
else:
    print(f"MISMATCH: Missing {expected_bookings-found_bookings} bookings")
driver.quit()