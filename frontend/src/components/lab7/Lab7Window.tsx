import { FC, useState, useEffect } from "react";
import {
    Button,
    Group,
    NumberInput,
    Notification,
    Title,
    Divider,
} from "@mantine/core";
import axios from "axios";
import Tree from "react-d3-tree";

interface RedTreeNode {
    keys: number[];
    children: RedTreeNode[];
}

interface RedTreeData {
    name: string;
    children: RedTreeNode[];
}

const transformRedTreeToD3Data = (node: any | undefined): any => {
    if (!node) {
        return null;
    }

    return {
        name: node.name || "Пустой узел",
        attributes: {
            color: node.color,
        },
        children: node.children.map(transformRedTreeToD3Data),
    };
};
const renderCustomNode = ({ nodeDatum }: any) => {
    const fillColor =
        nodeDatum.attributes?.color === "Черный" ? "black" : "red";

    return (
        <g>
            <circle r="12" stroke="gray" fill={fillColor} strokeWidth="1.5" />
            <text fill="white" x="15" dy="4" fontSize="24" strokeWidth="0">
                {nodeDatum.name}
            </text>
        </g>
    );
};
export const Lab7Window: FC = () => {
    const [key, setKey] = useState<number>();
    const [del_key, setDelKey] = useState<number>();
    const [search_key, setSearchKey] = useState<number>();
    const [treeData, setTreeData] = useState<RedTreeData | null>(null);
    const [message, setMessage] = useState<string | null>(null);
    const getTreeStructure = async () => {
        try {
            const response = await axios.get(
                "http://0.0.0.0:3415/v1/lab_7/tree_structure"
            );
            const bTreeData = response.data.tree;
            setTreeData(bTreeData);
        } catch (error) {
            setMessage("Ошибка при получении структуры дерева");
        }
    };

    const insertKey = async () => {
        if (key !== null) {
            try {
                const response = await axios.post(
                    "http://0.0.0.0:3415/v1/lab_7/insert",
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

    const deleteKey = async () => {
        if (del_key !== null) {
            try {
                const response = await axios.post(
                    "http://0.0.0.0:3415/v1/lab_7/del",
                    null,
                    {
                        params: { del_key },
                    }
                );
                setMessage(response.data.message);
                getTreeStructure();
            } catch (error) {
                setMessage("Ошибка при удалении ключа");
            }
        }
    };

    const searchKey = async () => {
        if (search_key !== null) {
            try {
                const response = await axios.get(
                    "http://0.0.0.0:3415/v1/lab_7/search",
                    {
                        params: { key: search_key },
                    }
                );
                setMessage(response.data.message);
                getTreeStructure();
            } catch (error) {
                setMessage("Ошибка при поиске ключа");
            }
        }
    };
    const clearTree = async () => {
        try {
            const response = await axios.post(
                "http://0.0.0.0:3415/v1/lab_7/clear"
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
                "http://0.0.0.0:3415/v1/lab_7/random_fill"
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
            <Title style={{ textAlign: "center" }}>
                🔴⚫ Красно-черное дерево
            </Title>{" "}
            <Divider my="sm"></Divider>
            <Group justify="center">
                <NumberInput
                    value={key}
                    w={"100px"}
                    onChange={(value) => setKey(Number(value))}
                />
                <Button onClick={insertKey} color="green">
                    Вставить ключ
                </Button>
                <NumberInput
                    value={search_key}
                    w={"100px"}
                    onChange={(value) => setSearchKey(Number(value))}
                />
                <Button color="orange" onClick={searchKey}>
                    Поиск ключа
                </Button>
                <NumberInput
                    value={del_key}
                    w={"100px"}
                    onChange={(value) => setDelKey(Number(value))}
                />
                <Button color="red" onClick={deleteKey}>
                    Удалить ключ
                </Button>
                <Divider me={"xl"} />
                <Button onClick={clearTree}>Очистить дерево</Button>
                <Button onClick={randomFill}>
                    Заполнить случайными ключами
                </Button>
            </Group>
            {message && (
                <Notification
                    color="teal"
                    onClose={() => setMessage(null)}
                    style={{
                        position: "fixed",
                        bottom: 20,
                        left: 20,
                        zIndex: 1000,
                    }}
                >
                    {message}
                </Notification>
            )}
            <Divider my="sm"></Divider>
            <div
                style={{
                    height: "100vh",
                    backgroundColor: "gray",
                }}
            >
                {treeData ? (
                    <Tree
                        data={transformRedTreeToD3Data(treeData)}
                        orientation="vertical"
                        pathFunc="straight"
                        translate={{ x: 500, y: 50 }}
                        renderCustomNodeElement={renderCustomNode}
                    />
                ) : (
                    <div />
                )}
            </div>
        </div>
    );
};
