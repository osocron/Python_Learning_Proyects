import java.time.LocalDate

import shapeless.{::, HList, HNil, Poly1}

/**
  * Created by osocron on 9/21/16.
  */
object Comparator extends App {

  def toBinary(n: Int, res: List[Int]): List[Int] =
      if (n <= 0) res else toBinary(n / 2, n % 2 :: res)

  toBinary(24, List()).foreach(n => println(n + " "))

  //-----------------------------------------------------------------------------

  case class Product(sku: String,
                     expirationDate: LocalDate,
                     price: BigDecimal)

  def expirationDiscountItems(products: List[Product]) =
    products.filter { case Product(sku, expD, price) => expD == LocalDate.now() }

  val products = List(
    Product("1", LocalDate.now(), BigDecimal(100.0)),
    Product("2", LocalDate.now().plusDays(1), BigDecimal(50.0)),
    Product("3", LocalDate.now(), BigDecimal(20.0)))

  expirationDiscountItems(products).foreach(p =>
    println(s"Price for sku ${p.sku} is now ${p.price * 0.8}"))

  //-----------------------------------------------------------------------------

  object polyMap extends Poly1 {
    implicit def caseInt = at[Int]{ _ == true }
    implicit def caseNone = at[None.type]{ _ == true }
    implicit def caseDouble = at[Double]{ _ == true }
    implicit def caseBool = at[Boolean]{ _ == true }
  }

  val items = 0 :: None :: 0.0 :: true :: 0 :: 7 :: HNil
  items.map(polyMap)

  //-----------------------------------------------------------------------------

  val people = List(("James", 17), ("Lars", 13), ("Robert", 8))
  people.find{ case (name, age) => age >= 18 }
    .getOrElse(new ClassNotFoundException("Item not found"))

  //-----------------------------------------------------------------------------

  def from(n: Int): Stream[Int] = n #:: from(n + 1)
  def primes = from(1).filter(n => (2 until n).forall(x => n % x != 0))
  primes.take(50).foreach(println)

  //-----------------------------------------------------------------------------

  case class Custumer(id: Int, total: Int, couponCode: String)
  val custumers = List(
    Custumer(1,  200, "F20"),
    Custumer(2,  150, "P30"),
    Custumer(3,  100, "P50"),
    Custumer(4, 1120, "F15")
  )
  def applyDiscount(c: Custumer): (Custumer, BigDecimal) = c.couponCode match {
    case "F20" => (c, BigDecimal(20))
    case "F15" => (c, BigDecimal(15))
    case "P30" => (c, BigDecimal(c.total * 0.3))
    case "P50" => (c, BigDecimal(c.total * 0.5))
    case _     => (c, BigDecimal(0))
  }
  val withDiscount = custumers.map(applyDiscount)
  withDiscount.foreach { case (c, d) =>
    println(s"ID: ${c.id} Total: ${c.total} Discount: $d") }

  // ---------------------------------------------------------------------------
  // Being in love with the for x in y syntax in python I will try to recreate the
  // in function with much love

  implicit class RichInt(val i: Int) extends AnyVal {
    def in[T](s: Seq[T]): Boolean = s.contains(i)
  }

  if (1 in List(1,2,3,4,5)) println("In sequence")
  else println("Not in sequence")


}
