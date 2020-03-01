# coding=utf-8

# java伪代码多线程版本 (MapReduce底层原理)
'''
    map:
    for loop:
        new Thread(()->{
            param={origin_data1,origin_data1...}
            Class clz=class_path1.getClass();
            result=clz.getDeclareMethod(function_name,clz).invoke(clz.newInstace(),param); // 反射调用函数
            message_queue.enQueue(result);
        }).run();

    reduce:
    for loop:
        new Thread(()->{
            param={};
            if(message_queue.size()<number){ // this number should set by problem
                for(){ // times should set by problem or function
                    param.append((ResultClass)message_queue.deQueue());
                }
                Class clz=class_path2.getClass();
                result=clz.getDeclareMethod(function_name,clz).invoke(clz.newInstace(),param); // 反射调用函数
                message_queue.enQueue(result);
            }
        }).run();
'''
def _reduce(lis, func):
    if len(lis) < 2:
        return lis
    else:
        lis.insert(0, func(lis.pop(0), lis.pop(0)))
        return _reduce(lis, func)  # 非递归用for实现也可


def _map(lis, func):
    return [func(item) for item in lis]


def main():
    print(_reduce(list(range(5)), lambda x, y: x + y))
    print(_reduce(list(range(1, 10)), lambda x, y: x * y))
    print(_map(list(range(1, 10)), lambda x: x ** 2))
    print(_map(list(range(1, 5)), lambda x: x + 3))


if __name__ == '__main__':
    main()
