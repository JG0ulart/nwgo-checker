from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

f = open('nwgoip1.txt', 'r')
for ip in f:
    try:
        browser = webdriver.Chrome("chromedriver.exe")
        browser.get(f"http://{ip}")

        advanced = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="details-button"]')))
        advanced.click()
        go_to = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="proceed-link"]')))
        go_to.click()

        # ONU FIRMWARE VERMELHA
        try:
            onu_model = browser.find_element(By.ID, "hg_logo").text
            #LOGIN 802.11 FIRMWARE VERMELHA
            user_login = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="txt_Username"]')))
            pass_login = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="txt_Password"]')))

            user_login.send_keys("telecomadmin")
            pass_login.send_keys("admintelecom")

            login_ONU = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="button"]')))
            login_ONU.click()
            #ONU N VERMELHA
            if onu_model == 'HG8546M':              
                wlan = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="headerTab"]/ul/li[5]/div[2]')))
                wlan.click()

                browser.switch_to.frame('frameContent')
                # VERIFY WLAN 2.4
                enable_verify0 = browser.find_element(By.XPATH, '//*[@id="wlEnbl"]')
                if enable_verify0.is_selected():
                    nwgo = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="record_1"]')))
                    nwgo.click()

                    enable = browser.find_element(By.XPATH, '//*[@id="wlEnable"]')
                    if enable.is_selected():
                        print('netway go da 2.4 ja esta ativado')                        
                    else:    
                        enable.click()
                        apply = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnApplySubmit"]')))
                        apply.click()
                        sleep(5)
                        
                else:
                    enable_verify0.click()
                    wifi_client = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="record_0"]'))) 
                    wifi_client.click()
                    wifi_client_enable = browser.find_element(By.XPATH, '//*[@id="wlEnable"]')
                    if wifi_client_enable.is_selected():
                        wifi_client_enable.click()
                        apply_wifi = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnApplySubmit"]')))
                        apply_wifi.click()                 
                        sleep(5)
                        nwgo = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="record_1"]')))
                        nwgo.click()

                        enable = browser.find_element(By.XPATH, '//*[@id="wlEnable"]')
                        if enable.is_selected():
                            print('netway go da 2.4 ja esta ativado')
                        else:    
                            enable.click()
                            apply = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnApplySubmit"]')))
                            apply.click()
                            sleep(5)
                        
                    else:
                        print('wifi do cliente ja estava desativado,  foi necessario ativar o WLAN da 2.4')
                                               
                        nwgo = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="record_1"]')))
                        nwgo.click()

                        enable = browser.find_element(By.XPATH, '//*[@id="wlEnable"]')
                        if enable.is_selected():
                            print('netway go da 2.4 ja esta ativado')
                        else:    
                            enable.click()
                            apply = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnApplySubmit"]')))
                            apply.click()
                            sleep(5)
                browser.quit()
                g = open('modelos.txt', 'a')
                g.write(f'{ip}, ONU firmware vermelha, modelo 802.11n ativou com sucesso. \n')
            #ONU AC FIRMWARE VERMELHA    
            else:
                wlan = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="headerTab"]/ul/li[5]/div[2]')))
                wlan.click()

                browser.switch_to.frame('frameContent')
                # VERIFY WLAN 2.4
                enable_verify0 = browser.find_element(By.XPATH, '//*[@id="wlEnbl"]')
                if enable_verify0.is_selected():
                    nwgo = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="record_1"]')))
                    nwgo.click()

                    enable = browser.find_element(By.XPATH, '//*[@id="wlEnable"]')
                    if enable.is_selected():
                        print('netway go da 2.4 ja esta ativado')
                    else:    
                        enable.click()
                        apply = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnApplySubmit"]')))
                        apply.click()
                        sleep(5)
                        
                else:
                    enable_verify0.click()
                    wifi_client = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="record_0"]'))) 
                    wifi_client.click()
                    wifi_client_enable = browser.find_element(By.XPATH, '//*[@id="wlEnable"]')
                    if wifi_client_enable.is_selected():
                        wifi_client_enable.click()
                        apply_wifi = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnApplySubmit"]')))
                        apply_wifi.click()                 
                        sleep(5)
                        nwgo = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="record_1"]')))
                        nwgo.click()

                        enable = browser.find_element(By.XPATH, '//*[@id="wlEnable"]')
                        if enable.is_selected():
                            print('netway go da 2.4 ja esta ativado')
                        else:    
                            enable.click()
                            apply = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnApplySubmit"]')))
                            apply.click()
                            sleep(5)
                        
                    else:
                        print('wifi do cliente ja estava desativado,  foi necessario ativar o WLAN da 2.4')
                                               
                        nwgo = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="record_1"]')))
                        nwgo.click()

                        enable = browser.find_element(By.XPATH, '//*[@id="wlEnable"]')
                        if enable.is_selected():
                            print('netway go da 2.4 ja esta ativado')
                        else:    
                            enable.click()
                            apply = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnApplySubmit"]')))
                            apply.click()
                            sleep(5)
                
                #CONFIG 5G
                browser.switch_to.default_content()
                w5g = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nav"]/ul/li[3]/div')))
                w5g.click()
                
                browser.switch_to.frame('frameContent')
                #VERIFY WLAN 5G
                enable_verify1 = browser.find_element(By.XPATH, '//*[@id="wlEnbl"]')
                if enable_verify1.is_selected():
                    print('wlan já está ativado, prosseguir para proxima parte')
                    nwgo_5g = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="record_3"]')))
                    nwgo_5g.click()
                    
                    enable_5g = browser.find_element(By.XPATH, '//*[@id="wlEnable"]')
                    if enable_5g.is_selected():
                        sleep(5)
                        browser.quit()
                        print(f'{ip}, já estava ativada a rede netway GO.')
                        g = open('modelos.txt', 'a')
                        g.write(f'{ip}, ONU firmware vermelha, modelo 802.11ac já estava ativada a rede netway GO. \n')
                    else:
                        enable_5g.click()                   
                        apply_5g = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnApplySubmit"]')))
                        apply_5g.click()                 
                        sleep(5)
                    
                        browser.quit()
                        g = open('modelos.txt', 'a')
                        g.write(f'{ip}, ONU firmware vermelha, modelo 802.11ac ativou com sucesso. \n')
                else:
                    enable_verify1.click()
                    print('ativei o wlan')
                    wifi_client5g = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="record_2"]'))) 
                    wifi_client5g.click()
                    
                    wifi_client_enable5g = browser.find_element(By.XPATH, '//*[@id="wlEnable"]')
                    if wifi_client_enable5g.is_selected():
                        wifi_client_enable5g.click()
                        apply_wifi = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnApplySubmit"]')))
                        apply_wifi.click()                 
                        sleep(5)
                        
                    else:
                        print('wifi do cliente ja estava desativado,  foi necessario ativar o WLAN  da 5g')
                               
                    nwgo_5g = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="record_3"]')))
                    nwgo_5g.click()
                    
                    enable_5g = browser.find_element(By.XPATH, '//*[@id="wlEnable"]')
                    if enable_5g.is_selected():
                        browser.quit()
                        g = open('modelos.txt', 'a')
                        g.write(f'{ip}, ONU firmware vermelha, modelo 802.11ac já estava ativada a rede netway GO, foi necessario ativar o WLAN 5g. \n')
                    else:
                        enable_5g.click()                   
                        apply_5g = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnApplySubmit"]')))
                        apply_5g.click()                 
                        sleep(5)
                    
                        browser.quit()
                        g = open('modelos.txt', 'a')
                        g.write(f'{ip}, ONU firmware vermelha, modelo 802.11ac ativou com sucesso, foi necessario ativar o WLAN 5g. \n')
                    
                    
        # ONU FIRMWARE AZUL
        except:
            onu_model = browser.find_element(By.ID, "ProductName").text
            
            user_login = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="txt_Username"]')))
            pass_login = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="txt_Password"]')))

            user_login.send_keys("telecomadmin")
            pass_login.send_keys("admintelecom")

            login_ONU = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginbutton"]')))
            login_ONU.click()


            config = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="name_addconfig"]')))
            config.click()
            
            wlan = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="name_wlanconfig"]')))
            wlan.click()

            browser.switch_to.frame('menuIframe')
            # VERIFY 2.4
            enable_verify0 = browser.find_element(By.XPATH, '//*[@id="wlEnbl"]')
            if enable_verify0.is_selected():
                nwgo = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="record_1"]')))
                nwgo.click()

                enable = browser.find_element(By.XPATH, '//*[@id="wlEnable"]')
                if enable.is_selected():
                    print('netway go da 2.4 ja esta ativado')
                else:    
                    enable.click()
                    apply = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnApplySubmit"]')))
                    apply.click()
                    sleep(5)
                    
            else:
                enable_verify0.click()
                wifi_client = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="record_0"]'))) 
                wifi_client.click()
                wifi_client_enable = browser.find_element(By.XPATH, '//*[@id="wlEnable"]')
                if wifi_client_enable.is_selected():
                    wifi_client_enable.click()
                    apply_wifi = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnApplySubmit"]')))
                    apply_wifi.click()                 
                    sleep(5)
                    nwgo = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="record_1"]')))
                    nwgo.click()

                    enable = browser.find_element(By.XPATH, '//*[@id="wlEnable"]')
                    if enable.is_selected():
                        print('netway go da 2.4 ja esta ativado')
                    else:    
                        enable.click()
                        apply = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnApplySubmit"]')))
                        apply.click()
                        sleep(5)
                    
                else:
                    print('wifi do cliente ja estava desativado,  foi necessario ativar o WLAN da 2.4')
                                            
                    nwgo = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="record_1"]')))
                    nwgo.click()

                    enable = browser.find_element(By.XPATH, '//*[@id="wlEnable"]')
                    if enable.is_selected():
                        print('netway go da 2.4 ja esta ativado')
                    else:    
                        enable.click()
                        apply = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnApplySubmit"]')))
                        apply.click()
                        sleep(5)
            
            
            #CONFIG 5G
            browser.switch_to.default_content()
            w5g = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wlan5basic"]')))
            w5g.click()
            
            browser.switch_to.frame('menuIframe')
            enable_verify1 = browser.find_element(By.XPATH, '//*[@id="wlEnbl"]')
            if enable_verify1.is_selected():
                print('wlan já está ativado, prosseguir para proxima parte')
                nwgo_5g = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="record_3"]')))
                nwgo_5g.click()
                
                enable_5g = browser.find_element(By.XPATH, '//*[@id="wlEnable"]')
                if enable_5g.is_selected():
                    browser.quit()
                    g = open('modelos.txt', 'a')
                    g.write(f'{ip}, ONU firmware azul, modelo 802.11ac já estava ativada a rede netway GO. \n')
                else:
                    enable_5g.click()                   
                    apply_5g = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnApplySubmit"]')))
                    apply_5g.click()                 
                    sleep(5)
                
                    browser.quit()
                    g = open('modelos.txt', 'a')
                    g.write(f'{ip}, ONU firmware azul, modelo 802.11ac ativou com sucesso. \n')
            else:
                enable_verify1.click()
                print('ativei o wlan')
                wifi_client5g = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="record_2"]'))) 
                wifi_client5g.click()
                
                wifi_client_enable5g = browser.find_element(By.XPATH, '//*[@id="wlEnable"]')
                if wifi_client_enable5g.is_selected():
                    wifi_client_enable5g.click()
                    apply_wifi = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnApplySubmit"]')))
                    apply_wifi.click()                 
                    sleep(5)
                    
                else:
                    print('wifi do cliente ja estava desativado,  foi necessario ativar o WLAN  da 5g')
                            
                nwgo_5g = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="record_3"]')))
                nwgo_5g.click()
                
                enable_5g = browser.find_element(By.XPATH, '//*[@id="wlEnable"]')
                if enable_5g.is_selected():
                    browser.quit()
                    g = open('modelos.txt', 'a')
                    g.write(f'{ip}, ONU firmware azul, modelo 802.11ac já estava ativada a rede netway GO, foi necessario ativar o WLAN 5g. \n')
                else:
                    enable_5g.click()                   
                    apply_5g = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnApplySubmit"]')))
                    apply_5g.click()                 
                    sleep(5)            
                    browser.quit()
                    g = open('modelos.txt', 'a')
                    g.write(f'{ip}, ONU firmware azul, modelo 802.11ac ativou com sucesso \n')

        finally:
            browser.quit()
    except:
        g = open('logs.txt', 'a')
        g.write(f'{ip}, nao funcionou, favor verificar. \n')