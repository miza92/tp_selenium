from selenium import webdriver
from selenium.webdriver.common.by import By
import logging

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait



def test_tp_books_amazon():
    # AAA
    # Arrange
    amazon_url = "http://www.amazon.fr"
    cookie_button_selector = "#sp-cc-accept"
    nav_hamburger_nemu = "#nav-hamburger-menu"
    livres_selector = "a[data-menu-id='10']"
    tous_les_livres_selector = "ul.hmenu.hmenu-visible.hmenu-translateX li:nth-child(3)"
    nouveautes__livre_selector = "div.a-section.octopus-pc-item-hue-shield.octopus-pc-item-image-background-v3"
    ajouter_au_panier_selector = "input#add-to-cart-button"
    aller_au_panier_selector = "a.a-button-text"
    quantite_selector = "span.a-button-text.a-declarative"
    select_quantity_selecotor = "select#quantity"
    keyword = "Qté:2"

    # Act
    driver = webdriver.Chrome()
    driver.get(amazon_url)
    driver.find_element(By.CSS_SELECTOR, cookie_button_selector).click()
    driver.find_element(By.CSS_SELECTOR, nav_hamburger_nemu).click()
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, livres_selector)))
    driver.find_element(By.CSS_SELECTOR, livres_selector).click()
    driver.find_element(By.CSS_SELECTOR, tous_les_livres_selector).click()
    driver.find_elements(By.CSS_SELECTOR, nouveautes__livre_selector)[0].click()
    driver.find_element(By.CSS_SELECTOR, ajouter_au_panier_selector).click()
    driver.find_element(By.CSS_SELECTOR, aller_au_panier_selector).click()
    driver.find_element(By.CSS_SELECTOR, quantite_selector).click()
    choisir_quantite = Select(driver.find_element(By.CSS_SELECTOR, select_quantity_selecotor))
    choisir_quantite.select_by_visible_text("2")
    quantite2 = driver.find_element(By.CSS_SELECTOR, quantite_selector).text

    # Assert
    assert quantite2 == keyword, "Le keyword et le resultat de la recherche sont differents"
    driver.quit()


