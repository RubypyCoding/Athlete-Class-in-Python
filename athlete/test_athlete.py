import unittest
from athlete import *


class AthleteTests(unittest.TestCase):

	def setUp(self):
		self.athlete_1 = Athlete()

	def test_total_distance_has_value_equal_to_zero_by_default(self):
		self.assertEqual(self.athlete_1.total_distance, 0)

	def test_total_time_has_value_equal_to_zero_by_default(self):
		self.assertEqual(self.athlete_1.total_time, 0)

	def test_validate_time_if_validate_time_raise_an_exception(self):
		with self.assertRaises(Exception):
			self.athlete_2 = Athlete(0, 10)
			self.athlete_2.validate_time()

class RunnerTests(unittest.TestCase):

	def setUp(self):
		self.runner_1 = Runner()
		self.runner_2 = Runner(10,10)

	def test_total_distance_has_value_equal_to_zero_by_default(self):
		self.assertEqual(self.runner_1.total_distance, 0)

	def test_total_time_has_value_equal_to_zero_by_default(self):
		self.assertEqual(self.runner_1.total_time, 0)

	def test_validate_time_if_validate_time_raise_an_exception(self):
		with self.assertRaises(Exception):
			self.runner_3 = Runner(0, 10)
			self.runner_3.validate_time()

	def test_speed_speed_as_getter(self):
		raised = False
		try:
			self.runner_1.speed
		except:
			raised = True
		self.assertFalse(raised, "Exception Raised")

	def test_speed_speed_as_setter(self):
		raised = False
		try:
			self.runner_1.speed = 0
		except:
			raised = True
		self.assertFalse(raised, "Exception Raised")

	def test_total_time_total_time_as_getter(self):
		raised = False
		try:
			self.runner_1.total_time
		except:
			raised = True
		self.assertFalse(raised, "Exception Raised")

	def test_total_time_total_time_as_setter(self):
		raised = False
		try:
			self.runner_1.total_time = 20
		except:
			raised = True
		self.assertFalse(raised, "Exception Raised")

	def test_speed_record_if_speed_record_exists(self):
		raised = False
		try:
			self.runner_1.speed_record()
		except:
			raised = True
		self.assertFalse(raised, "Exception Raised")

	def test_total_distance_total_distance_as_getter(self):
		raised = False
		try:
			self.runner_1.total_distance
		except:
			raised = True
		self.assertFalse(raised, "Exception Raised")

	def test_total_distance_total_distance_as_setter(self):
		raised = False
		try:
			self.runner_1.total_distance = 10
		except:
			raised = True
		self.assertFalse(raised, "Exception Raised")

	def test_run_returns_a_string_with_total_distance_total_time_and_speed_when_distance_0_and_time_0(self):
		self.assertEqual(self.runner_1.run(), "I'm a Runner and Ran 0 meters, time: 0 seconds, speed: 0 m/s")

	def test_run_returns_a_string_with_total_distance_total_time_and_speed_when_distance_greater_than_0_and_time_greater_than_0(self):
		self.assertEqual(self.runner_2.run(), "I'm a Runner and Ran 10 meters, time: 10 seconds, speed: 1.0 m/s")

	def test_new_workout_if_new_workout_increments_total_distance_and_total_time(self):
		raised = False
		try:
			self.runner_1.new_workout(20, 7)
		except:
			raised = True
		self.assertFalse(raised, "Exception Raised")
		self.assertEqual(self.runner_1.run(), "I'm a Runner and Ran 20 meters, time: 7 seconds, speed: 2.86 m/s")

class SwimmerTests(unittest.TestCase):

	#evaluar el nombre recibido para Swimmer OJOOOOO




	# def test_name_is_evaluated_as_getter(self):
	#     self.assertEqual(self.func_1.name, "Amex")

	# def test_name_is_evaluated_as_setter(self):
	# 	with self.assertRaises(AttributeError):
	# 	    self.func_1.name = "Amex to Go"

	# def test_number_is_evaluated_as_getter(self):
	#     self.assertEqual(self.func_1.number, "2345673444")

	# def test_number_is_evaluated_as_setter(self):
	# 	with self.assertRaises(AttributeError):
	# 	    self.func_1.number = "2345677447"

	# def test_expiration_is_evaluated_as_getter(self):
	#     self.assertEqual(self.func_1.expiration, "12/15")

	# def test_expiration_is_evaluated_as_setter(self):
	# 	with self.assertRaises(AttributeError):
	# 	    self.func_1.expiration = "12/23"

	# def test_cvc_is_evaluated_as_getter(self):
	#     self.assertEqual(self.func_1.cvc, "2345")

	# def test_expiration_is_evaluated_as_setter(self):
	# 	with self.assertRaises(AttributeError):
	# 	    self.func_1.cvc = "2347"

	# def test_status_is_evaluated_as_getter(self):
	#     self.assertEqual(self.func_1.status, [234, 567, 456, 567, 344])

	# def test_status_is_evaluated_as_setter(self):
	#     raised = False
	#     try:
	#     	self.func_1 = [234, 567, 456, 567, 980]
	#     except:
	#     	raised = True
	#     self.assertFalse(raised, "Exception raised")

	# def test_total_status_returns_total_of_balances_of_creditcard(self):
	# 	self.assertEqual(self.func_2.total_status(), 1946)


# class PortfolioTests(unittest.TestCase):

# 	def setUp(self):
# 		self.func_amex = CreditCard("Amex", "2345673444", "12/15", "2345", [234, 567, 456, 567, 344])
# 		self.func_bancomer = CreditCard("Bancomer", "2345673444", "12/15", "2645", [234, 345, 456, 567, 344])
# 		self.func_scotiabank = CreditCard("ScotiaBank", "2345673744", "12/16", "2845", [234, 345, 456, 567, 344])
# 		self.func_serfin = CreditCard("Serfin", "2345473454", "12/20", "1345", [234, 345, 456, 567, 344])
# 		self.func_bancoppel = CreditCard("BanCoppel", "2345373464", "12/18", "2445", [567, 345, 456, 567, 344])
# 		self.func_banregio = CreditCard("BanRegio", "2345373464", "12/18", "2445", [567, 345, 456, 567, 344])
# 		self.func_portfolio = Portfolio([self.func_amex, self.func_scotiabank, self.func_bancomer, self.func_serfin, self.func_bancoppel])

# 	def test_how_many_cards_if_how_many_cards_returns_total_of_creditcards_in_portfolio(self):
# 		self.assertEqual(self.func_portfolio.how_many_cards(), 5)

# 	def test_add_creditcard_if_add_creditcard_adds_a_new_creditcard_in_portfolio(self):
# 		raised = False
# 		try:
# 			self.func_portfolio.add_creditcard(self.func_banregio)
# 		except:
# 			raised = True
# 		self.assertFalse(raised, "Exception raised")
# 		self.assertEqual(self.func_portfolio.how_many_cards(), 6)

# 	def test_sum_portfolio_if_sum_portfolio_returns_total_balances_of_portfolio(self):
# 		self.func_portfolio.add_creditcard(self.func_banregio)
# 		self.assertEqual(self.func_portfolio.sum_portfolio(), 12564)

# 	def test_delete_creditcard_if_delete_creditcard_drops_a_creditcard_from_portfolio(self):
# 		self.func_portfolio.add_creditcard(self.func_banregio)
# 		raised = False
# 		try:
# 			self.func_portfolio.delete_creditcard("Bancomer")
# 		except:
# 			raised = True
# 		self.assertFalse(raised, "Exception raised")
# 		self.assertEqual(self.func_portfolio.how_many_cards(), 5)
# 		self.assertEqual(self.func_portfolio.sum_portfolio(), 10618)


if __name__=="__main__":
    unittest.main()