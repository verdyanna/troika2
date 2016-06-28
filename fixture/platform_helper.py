class PlatformHelper:

    def __init__(self, app):
        self.app = app


    def fill_new_platform_form(self):
        wd = self.app.wd
        wd.find_element_by_link_text(u"Начать работу").click()
        wd.find_element_by_id("add-object").click()
        wd.find_element_by_id("id_address").click()
        wd.find_element_by_id("id_address").clear()
        wd.find_element_by_id("id_address").send_keys("г Москва, проезд Красногорский 1-й ")

        wd.find_element_by_id("id_mkd").click()
        wd.find_element_by_id("ui-id-9").click()
        wd.find_element_by_id("id_qty_container").click()
        wd.find_element_by_id("id_qty_container").clear()
        wd.find_element_by_id("id_qty_container").send_keys("5")

        wd.find_element_by_id("id_capacity_container").click()
        wd.find_element_by_id("ui-id-18").click()
        wd.find_element_by_id("id_type").click()
        wd.find_element_by_id("ui-id-21").click()
        wd.find_element_by_id("id_surface").click()
        wd.find_element_by_id("ui-id-25").click()
        wd.find_element_by_id("id_fences").click()
        wd.find_element_by_id("ui-id-32").click()
        wd.find_element_by_id("id_place_kgm").click()
        wd.find_element_by_id("ui-id-35").click()
        wd.find_element_by_id("id_dispose").click()
        wd.find_element_by_id("ui-id-36").click()
        wd.find_element_by_id("id_org_1").click()
        wd.find_element_by_id("id_org_1").clear()
        wd.find_element_by_id("id_org_1").send_keys("\"АВГУСТ\" ООО")
        wd.find_element_by_css_selector("span.suggestions-subtext.suggestions-subtext_inline").click()
        wd.find_element_by_id("id_org_2").click()
        wd.find_element_by_id("id_org_2").clear()
        wd.find_element_by_id("id_org_2").send_keys("\"АВЕЛОКС\" ООО")
        wd.find_element_by_xpath("//div[@class='ins']//span[.='\"АВЕЛОКС\" ООО']").click()
        wd.find_element_by_id("save-object").click()
        wd.find_element_by_css_selector("a.fancybox-item.fancybox-close").click()
        wd.find_element_by_id("save-object").click()

