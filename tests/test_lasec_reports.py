# -*- encoding: utf-8 -*-

from openerp.tests.common import TransactionCase


class TestLasec(TransactionCase):

    # Method seudo-constructor of test setUp
    def setUp(self):
        # Define global variables to tests
        super(TestLasec, self).setUp()
        self.variable = "hello world"
        self.report = self.env['lasec.invoice']


    # Method of class that don´t is test
    def create_report(self, report_name):
        report_id = self.course.create({
            'name': name,
        })
        return report_id

    # Method of test startwith "def test_*(self)"
    def test_01_report_same_name(self):
        self.create_report('test', 'test', None)

