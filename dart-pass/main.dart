/* If the value you have is computed at runtime (new DateTime.now(), for example), you can not use a const for it. 

The right Solution:
main() {
DateTime now = DateTime.now();
print(now.hour.toString() + ":" + now.minute.toString() + ":" + now.second.toString());

}
  */
