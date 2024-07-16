from abc import ABC, abstractmethod


class NespressoAppSteps(ABC):

    @abstractmethod
    def handle_app_crash_on_launch(self, retries=3):
        pass

    @abstractmethod
    def handle_app_crash_on_log_in(self, retries=3):
        pass

    @abstractmethod
    def handle_location_permission(self, action='permanently'):
        pass

    @abstractmethod
    def is_permission_popup_appear(self) -> bool:
        pass

    @abstractmethod
    def handle_push_notification_popup(self):
        pass

    @abstractmethod
    def register_new_user(self, random_email):
        pass

    @abstractmethod
    def log_out(self):
        pass

    @abstractmethod
    def log_in(self, email):
        pass

    @abstractmethod
    def order_product(self):
        pass

    @abstractmethod
    def log_in_using_biometric(self):
        pass