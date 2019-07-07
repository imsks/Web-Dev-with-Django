from django.shortcuts import render
from django.views.generic import (TemplateView, )
import datetime

# returns current year
def getCurrentYear() :
    currYear = datetime.datetime.now()
    return currYear.year


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context_dict = {
            'title' : 'Pt. D D U S V M Inter College',
            'current_year' : getCurrentYear(),
        }
        return context_dict

class AboutUsView(TemplateView):
    template_name = 'about-us.html'

    def get_context_data(self, **kwargs):
        context_dict = {
            'title' : 'About us | Pt D D U S V M Inter College',
        }
        return context_dict

class MissionAndVision(TemplateView):
    template_name = 'mission-and-vision.html'

    def get_context_data(self, **kwargs):
        context_dict = {
            'title' : 'Mission & Vision | Pt D D U S V M Inter College',
        }
        return context_dict

class SchoolProfileView(TemplateView):
    template_name = 'school-profile.html'

    def get_context_data(self, **kwargs):
        context_dict = {
            'title' : 'School Profile | Pt D D U S V M Inter College',
        }
        return context_dict

class ManagementCommitteeView(TemplateView):
    template_name = 'management-committee-pages.html'
    
    def get_context_data(self, **kwargs):
        committee_data = {
            'title' : 'Management Committee | Pt D D U S V M Inter College',
            'page_1' : {
                'name' : {
                    1 : 'Ajay Kumar Aga',
                    2 : 'Ghanshyam Das Tolani',
                    3 : 'Sudesh Kumar Gupta',
                    4 : 'Ravi Bhushan Sahni',
                },
            },

            'page_2' : {
                'name' : {
                    5 : 'Vimal Agarwal',
                    6 : 'Vijay Ji Agarwal',
                    7 : 'Shipra Bajpai',
                    8 : 'Sheshdhar Dwivedi',
                },
            },

            'page_3' : {
                'name' : {
                    9 : 'Dinesh Agrawal',
                    10 : 'Mahaveer Prasad',
                    11 : 'Dr.Satish Kaushal Bajpai',
                    12 : 'Ajay'
                },
            },

            'designation' : {
                1 : '1',
                2 : 'Lecturer',
                3 : 'Manager',
                4 : 'Vice President',
                5 : 'Treasurer',
                6 : 'Member',
                7 : 'N/A',
            },

            'occupation' : {
                1 : 'Teacher',
                2 : 'Business',
                3 : 'Principal',
                4 : 'Doctor'
            },


        }
        return committee_data

class AdmissionView(TemplateView):
    template_name = 'admission.html'

    def get_context_data(self, **kwargs):
        context_dict = {
            'title' : 'Admission | Pt D D U S V M Inter College',
        }
        return context_dict

class RulesAndRegulations(TemplateView):
    template_name = 'rules-and-regulations.html'

    def get_context_data(self, **kwargs):
        context_dict = {
            'title' : 'Rules & Regulations | Pt D D U S V M Inter College',
        }
        return context_dict

class SyllabusView(TemplateView):
    template_name = 'syllabus.html'

    def get_context_data(self, **kwargs):
        context_dict = {
            'title' : 'Syllabus | Pt D D U S V M Inter College',
        }
        return context_dict

class FacilitiesView(TemplateView):
    template_name = 'facilities.html'

    def get_context_data(self, **kwargs):
        context_dict = {
            'title' : 'Facilities | Pt D D U S V M Inter College',
        }
        return context_dict

class ExaminationsView(TemplateView):
    template_name = 'examinations.html'

    def get_context_data(self, **kwargs):
        context_dict = {
            'title' : 'Examinations | Pt D D U S V M Inter College',
        }
        return context_dict

class ResultsView(TemplateView):
    template_name = 'results.html'

    def get_context_data(self, **kwargs):
        context_dict = {
            'title' : 'Results | Pt D D U S V M Inter College',
        }
        return context_dict

class LibraryView(TemplateView):
    template_name = 'library.html'

class labsView(TemplateView):
     template_name = 'labs.html'

     def get_context_data(self, **kwargs):
        context_dict = {
            'title' : 'Labs | Pt D D U S V M Inter College',
        }
        return context_dict

class VideoGallery(TemplateView):
    template_name = 'video-gallery.html'

    def get_context_data(self, **kwargs):
        context_dict = {
            'title' : 'Video Gallery | Pt D D U S V M Inter College',
        }
        return context_dict

class ImageGallery(TemplateView):
    template_name = 'image-gallery.html'

    def get_context_data(self, **kwargs):
        context_dict = {
            'title' : 'Image Gallery | Pt D D U S V M Inter College',
        }
        return context_dict

class AdmissionEnquiryView(TemplateView):
    template_name = 'admission-enquiry.html'

    def get_context_data(self, **kwargs):
        context_dict = {
            'title' : 'Admission Enquiry | Pt D D U S V M Inter College',
        }
        return context_dict

class NoticeBoardView(TemplateView):
    template_name = 'notice-board.html'

    def get_context_data(self, **kwargs):
        context_dict = {
            'title' : 'Notice Board | Pt D D U S V M Inter College',
        }
        return context_dict

class StudentDetailsView(TemplateView):
    template_name = 'student-details.html'

    def get_context_data(self, **kwargs):
        context_dict = {
            'title' : 'Student Details | Pt D D U S V M Inter College',
        }
        return context_dict

class ContactUsView(TemplateView):
    template_name = 'contact-us.html'

    def get_context_data(self, **kwargs):
        context_dict = {
            'title' : 'Contact Us | Pt D D U S V M Inter College',
        }
        return context_dict

class FeeRulesView(TemplateView):
    template_name = 'fee-rules.html'

    def get_context_data(self, **kwargs):
        context_dict = {
            'title' : 'Fee rules | Pt D D U S V M Inter College',
        }
        return context_dict

class DisiplinaryRulesView(TemplateView):
    template_name = 'disiplinary-rules.html'

    def get_context_data(self, **kwargs):
        context_dict = {
            'title' : 'Disiplinary Rules | Pt D D U S V M Inter College',
        }
        return context_dict

class EventsView(TemplateView):
    template_name = 'events.html'

    def get_context_data(self, **kwargs):
        context_dict = {
            'title' : 'Events | Pt D D U S V M Inter College',
        }
        return context_dict

class NewsAndUpdatesView(TemplateView):
    template_name = 'news-and-updates.html'

    def get_context_data(self, **kwargs):
        context_dict = {
            'title' : 'News and Updates | Pt D D U S V M Inter College',
        }
        return context_dict 


class CalenderView(TemplateView):
    template_name = 'calender.html'

    def get_context_data(self, **kwargs):
        context_dict = {
            'title' : 'Calender | Pt D D U S V M Inter College',
        }
        return context_dict 

class PrivacyPolicyView(TemplateView):
    template_name = 'privacy-policy.html'

    def get_context_data(self, **kwargs):
        context_dict = {
            'title' : 'Privacy Policy | Pt D D U S V M Inter College',
        }
        return context_dict 

class TermsOfUseView(TemplateView):
    template_name = 'terms-of-use.html'

    def get_context_data(self, **kwargs):
        context_dict = {
            'title' : 'Terms of use | Pt D D U S V M Inter College',
        }
        return context_dict 

class Sitemap(TemplateView):
    template_name = 'sitemap.html'

    def get_context_data(self, **kwargs):
        context_dict = {
            'title' : 'Sitemap | Pt D D U S V M Inter College',
        }
        return context_dict 