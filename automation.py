from seleniumbase import SB
import time

ss_count = 1

# Keep the SB context manager alive
_sb = None


def start():
    global _sb

    _sb = SB(uc=True)
    cortex = _sb.__enter__()

    def screenshot():
        global ss_count
        cortex.save_screenshot(f"screenshots/ss{ss_count:03}.png")
        ss_count += 1

    def wait():
        print("Waiting for response...")
        while cortex.is_element_visible('mat-icon[fonticon="stop"]'):
            time.sleep(0.05)
        print("Gemini finished!")

    cortex.open("https://gemini.google.com")
    
    #time.sleep(4)
   # cortex.driver.minimize_window()
    cortex.wait_for_element_visible('button[data-test-id="read-more-button"]')

    print(cortex.is_element_visible('button[data-test-id="read-more-button"]'))
    if cortex.is_element_visible('button[data-test-id="read-more-button"]'):
        cortex.click('button[data-test-id="read-more-button"]')
        time.sleep(1)

    if cortex.is_element_visible('[data-test-id="accept-button"]'):
        cortex.click('[data-test-id="accept-button"]')


    input_box = 'div.ql-editor[contenteditable="true"]'
    cortex.wait_for_element_visible(input_box)

    print("Gemini is ready!")

    def gemini(prompt):
        #screenshot()

        selector = 'div.ql-editor[contenteditable="true"]'

        cortex.wait_for_element_visible(selector)
        cortex.click(selector)

        for ch in prompt:
            cortex.send_keys(selector, ch)
            time.sleep(0.02)

        cortex.click('button[aria-label="Send message"]')

        wait()

        return cortex.find_elements("message-content")[-1].text
    

    return gemini


'''if __name__ == "__main__":
    bot = start()

    print("Type 'exit' to quit.\n")

    while True:
        msg = input("You: ")

        if msg.lower() in ("exit", "quit"):
            break

        print(f"Gemini: {bot(msg)}")'''

    
