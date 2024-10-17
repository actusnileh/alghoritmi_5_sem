import {
    Container,
    Title,
    TextInput,
    Button,
    Notification,
} from "@mantine/core";
import { FC, useEffect, useState } from "react";
import axios from "axios";
import Tree from "react-d3-tree";

export const Lab5Window: FC = () => {
    const [key, setKey] = useState<number>(0);
    const [value, setValue] = useState<number>(0);
    const [searchKey, setSearchKey] = useState<number>(0);
    const [notification, setNotification] = useState<{
        message: string;
        color: string;
    } | null>(null);
    const [treeData, setTreeData] = useState<any>(null); // Данные для визуализации

    const fetchTree = async () => {
        try {
            const response = await axios.get("http://0.0.0.0:8000/v1/lab_5/");
            const formattedTreeData = formatTreeData(response.data.keys);
            setTreeData(formattedTreeData);
        } catch (error) {
            setNotification({
                message: "Ошибка получения дерева",
                color: "red",
            });
        }
    };

    const formatTreeData = (keys: any[]) => {
        const root = { name: "Root", children: [] };
        const map: { [key: string]: any } = { Root: root };

        keys.forEach(({ key, value }) => {
            const nodeName = `Key: ${key}, Value: ${value}`;
            const node = { name: nodeName };
            map[nodeName] = node;
            root.children.push(node);
        });

        return root;
    };

    const handleInsert = async () => {
        try {
            await axios.post("http://0.0.0.0:8000/v1/lab_5/insert", null, {
                params: { key, value },
            });
            setNotification({
                message: `Вставлено: ${key}`,
                color: "green",
            });
            fetchTree(); // Обновляем дерево после вставки
        } catch (error) {
            setNotification({ message: "Ошибка вставки", color: "red" });
        }
    };

    const handleSearch = async () => {
        try {
            const response = await axios.get(
                `http://0.0.0.0:8000/v1/lab_5/search`,
                {
                    params: { key: searchKey },
                }
            );
            setNotification({
                message: `Найдено: ${response.data.keys[0].key} = ${response.data.keys[0].value}`,
                color: "blue",
            });
        } catch (error) {
            setNotification({ message: "Ключ не найден", color: "red" });
        }
    };

    useEffect(() => {
        fetchTree(); // Загружаем дерево при монтировании компонента
    }, []);

    return (
        <Container
            my="xl"
            style={{
                alignItems: "center",
                textAlign: "center",
            }}
        >
            <Title order={2} mb="xl">
                Лаб. работа №5
            </Title>

            <TextInput
                placeholder="Ключ для вставки"
                label="Ключ"
                value={key}
                onChange={(e) => setKey(Number(e.currentTarget.value))}
                mb="md"
            />
            <TextInput
                placeholder="Значение для вставки"
                label="Значение"
                value={value}
                onChange={(e) => setValue(Number(e.currentTarget.value))}
                mb="md"
            />
            <Button onClick={handleInsert}>Вставить</Button>

            <TextInput
                placeholder="Ключ для поиска"
                label="Ключ для поиска"
                value={searchKey}
                onChange={(e) => setSearchKey(Number(e.currentTarget.value))}
                mb="md"
            />
            <Button onClick={handleSearch} mb="md">
                Поиск
            </Button>
            {notification && (
                <Notification
                    color={notification.color}
                    onClose={() => setNotification(null)}
                >
                    {notification.message}
                </Notification>
            )}

            {treeData && (
                <div
                    style={{
                        height: "500px",
                        marginTop: "20px",
                        backgroundColor: "white",
                        color: "black",
                        border: "1px solid #ccc",
                        borderRadius: "4px",
                    }}
                >
                    <Tree data={treeData} />
                </div>
            )}
        </Container>
    );
};
