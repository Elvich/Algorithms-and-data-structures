import DoublyLinkedList

class MedicalRecord:
    def __init__(self, first_name, last_name, diagnosis, admission_date, discharge_date, procedures, medications):
        self.first_name = first_name
        self.last_name = last_name
        self.diagnosis = diagnosis
        self.admission_date = admission_date
        self.discharge_date = discharge_date
        self.procedures = procedures  
        self.medications = medications

    def __str__(self):
        return (f"{self.first_name} {self.last_name} | Диагноз: {self.diagnosis} "
                f"| Поступил: {self.admission_date}, Выписан: {self.discharge_date} "
                f"| Процедуры: {', '.join(self.procedures)} "
                f"| Лекарства: {', '.join(self.medications)}")


patient_list = DoublyLinkedList.DoublyLinkedList()
patient_list.append(MedicalRecord("Иван", "Петров", "Грипп",
                                  "2025-04-01", "2025-04-06",
                                  ["анализ крови", "УЗИ"], ["аспирин", "витамин C"]))

patient_list.display_forward()