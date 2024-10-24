import { FC, useState, useEffect } from "react";
import { Button, Group, NumberInput, Notification } from "@mantine/core";
import axios from "axios";
import Tree from "react-d3-tree";

interface BTreeNode {
    keys: number[];
    children: BTreeNode[];
}

interface BTreeData {
    name: string;
    children: BTreeNode[];
}

// Функция для преобразования B-дерева в формат для react-d3-tree
const transformBTreeToD3Data = (node: any | undefined): any => {
    if (!node) {
        return null; // Если узел не определен, возвращаем null
    }

    // Изменяем структуру, чтобы использовать name вместо keys
    return {
        name: node.name || "Пустой узел", // Используем name из API
        children: node.children.map(transformBTreeToD3Data), // Рекурсивно преобразуем дочерние узлы
    };
};

export const Lab5Window: FC = () => {
    const [key, setKey] = useState<number>();
    const [treeData, setTreeData] = useState<BTreeData | null>(null);
    const [message, setMessage] = useState<string | null>(null);

    const getTreeStructure = async () => {
        try {
            const response = await axios.get(
                "http://0.0.0.0:8000/v1/lab_5/tree_structure"
            );
            console.log("B-Tree Data from API:", response.data); // Логируем данные
            const bTreeData = response.data.tree; // Получаем данные дерева
            console.log("Parsed B-Tree Data:", bTreeData); // Логируем, что мы получили
            setTreeData(bTreeData);
        } catch (error) {
            setMessage("Ошибка при получении структуры дерева");
        }
    };

    const insertKey = async () => {
        if (key !== null) {
            try {
                const response = await axios.post(
                    "http://0.0.0.0:8000/v1/lab_5/insert",
                    null,
                    {
                        params: { key },
                    }
                );
                setMessage(response.data.message);
                getTreeStructure();
            } catch (error) {
                setMessage("Ошибка при вставке ключа");
            }
        }
    };

    const clearTree = async () => {
        try {
            const response = await axios.post(
                "http://0.0.0.0:8000/v1/lab_5/clear"
            );
            setMessage(response.data.message);
            getTreeStructure();
        } catch (error) {
            setMessage("Ошибка при очистке дерева");
        }
    };

    const randomFill = async () => {
        try {
            const response = await axios.post(
                "http://0.0.0.0:8000/v1/lab_5/random_fill"
            );
            setMessage(response.data.message);
            getTreeStructure();
        } catch (error) {
            setMessage("Ошибка при заполнении случайными ключами");
        }
    };

    useEffect(() => {
        getTreeStructure();
    }, []);

    return (
        <div>
            <h1>B-дерево Визуализация</h1>

            <Group>
                <NumberInput value={key} onChange={(value) => setKey(value)} />
                <Button onClick={insertKey}>Вставить ключ</Button>
                <Button onClick={clearTree}>Очистить дерево</Button>
                <Button onClick={randomFill}>
                    Заполнить случайными ключами
                </Button>
            </Group>

            {message && (
                <Notification color="teal" onClose={() => setMessage(null)}>
                    {message}
                </Notification>
            )}

            <div
                style={{
                    height: "100vh", // Высота на 100% экрана, минус отступ сверху
                    backgroundColor: "gray",
                }}
            >
                {treeData ? (
                    <Tree
                        data={transformBTreeToD3Data(treeData)}
                        orientation="vertical"
                        pathFunc="straight"
                        translate={{ x: 500, y: 50 }}
                    />
                ) : (
                    <div style={{ color: "white" }}>Дерево пусто</div>
                )}
            </div>
        </div>
    );
};
